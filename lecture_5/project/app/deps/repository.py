from db.database import SessionLocal
from fastapi import Depends
from repositories.sqlalchemy_book_repository import (
    SQLAlchemyBookRepository,
)
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_book_repository(
    db: Session = Depends(get_db),
) -> SQLAlchemyBookRepository:
    return SQLAlchemyBookRepository(db)
