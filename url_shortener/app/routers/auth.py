from typing import Union
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer

import bcrypt

from sqlalchemy.orm import Session
from pydantic import BaseModel
from jose import JWTError, jwt
from database import get_db
from datetime import datetime, timedelta
import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/signin")
oauth2_scheme_optional = OAuth2PasswordBearer(tokenUrl="/signin", auto_error=False)

router = APIRouter()


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "edaede757923443710104595e3fc883901d77ffd551776e4a8382cec9cead341"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class User(BaseModel):
    username: str
    password: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInDB(User):
    hashed_password: str


def fake_hash_password(password: str):
    return "fakehashed" + password


def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    return token_data


@router.post("/users/signup", tags=["User"])
async def signup(User: User, db: Session = Depends(get_db)):
    hashed_password = get_hashed_password(User.password)

    user_model = models.Users()
    user_model.username = User.username
    user_model.hashed_password = hashed_password

    db.add(user_model)
    db.commit()

    return {
        "status": "success",
        "message": f"User with {user_model.username} has been created",
    }


@router.post("/signin", tags=["User"])
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = (
        db.query(models.Users)
        .filter(models.Users.username == form_data.username)
        .first()
    )

    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = db_user.__dict__

    password_match = check_password(
        form_data.password,
        user["hashed_password"],
    )

    if not password_match:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
