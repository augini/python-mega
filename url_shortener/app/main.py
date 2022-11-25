import models
from routers import auth, urls

from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException

from database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI(
    title="Qisqa URL",
    description="Shorten your urls with qisqaurl.pro in the shortest time possible",
    version="0.0.1",
    terms_of_service="https://qisqaurl.pro",
    contact={
        "name": "Atabekov Farrukh",
        "url": "https://atabekov.com",
        "email": "atabekov@protonmail.com",
    },
)

app.include_router(auth.router)
app.include_router(urls.router, prefix="/api/v1")

models.Base.metadata.create_all(bind=engine)


@app.get("/{hash_key}", tags=["Url"])
async def get_long_url(hash_key: str, db: Session = Depends(get_db)):

    long_url = db.query(models.Urls).filter(models.Urls.short == hash_key).first()

    if long_url is not None:
        return RedirectResponse(f"{long_url.url}")

    raise HTTPException(status_code=404, detail=f"Url for {hash_key} doesn't exist")


@app.get("/ping")
def get_status():
    return "pong"
