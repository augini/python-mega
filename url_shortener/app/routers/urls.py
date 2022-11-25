from config import Settings
import models
from .auth import get_current_user, oauth2_scheme_optional, oauth2_scheme

from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel, Field

from database import get_db
from sqlalchemy.orm import Session

from hashlib import sha256
from validators import url
from base64 import b64encode

router = APIRouter()

settings = Settings()


class URL(BaseModel):
    long_url: str


@router.post("/short", tags=["Url"])
async def shorten_url(
    URL: URL,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme_optional),
):
    long_url = URL.long_url

    if long_url[:7] != "http://" and long_url[:8] != "https://":
        long_url = f"http://{long_url}"

    if not url(long_url):
        raise HTTPException(status_code=400, detail=f"Invalid url")

    prefix = None

    if token:
        token_data = await get_current_user(token)
        prefix = token_data.username
    else:
        prefix = str(db.query(models.Urls).count())

    exten_string = prefix + "+" + long_url

    hash_object = sha256(exten_string.encode()).hexdigest()
    hashed_key = b64encode(hash_object.encode()).decode()[:8]

    if not hashed_key:
        raise HTTPException(
            status_code=501, detail=f"Error shortening the provided url"
        )

    url_model = models.Urls()
    url_model.url = long_url
    url_model.short = hashed_key

    db.add(url_model)
    db.commit()

    return {
        "message": "success",
        "shortened_url": f"{settings.base_url}/{hashed_key}",
    }


@router.get("/urls", tags=["Url"])
def get_urls(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(models.Urls).all()
