from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

from datetime import datetime


class Urls(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    short = Column(String)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    created_at = Column(
        "timestamp", TIMESTAMP(timezone=False), nullable=False, default=datetime.now()
    )
