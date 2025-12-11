from custom_exceptions.exceptions import (
    BookNotCreatedError,
    BookNotFoundError,
    BookUpdateError,
)
from models.book import Book
from schemas.book import BookCreate, BookUpdated
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


class SQLAlchemyBookRepository:
    def __init__(self, db: Session):
        self.db = db

    # Get a single book by id
    def get(self, book_id: int) -> Book | None:
        return self.db.query(Book).filter(Book.id == book_id).first()

    # Get all books
    def list(self) -> list[Book]:
        return self.db.query(Book).all()

    # Create a new book
    def create(self, data: BookCreate) -> Book:
        book = Book(
            title=data.title, author=data.author, year=data.year
        )
        try:
            self.db.add(book)
            self.db.commit()
            self.db.refresh(book)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise BookNotCreatedError from e

        return book

    # Update an existing book by id
    def update(self, book_id: int, data: BookUpdated) -> Book | None:
        book = self.get(book_id)
        if not book:
            raise BookNotFoundError(book_id)

        updates = data.model_dump(exclude_unset=True)
        for key, value in updates.items():
            setattr(book, key, value)

        try:
            self.db.commit()
            self.db.refresh(book)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise BookUpdateError(book_id) from e

        return book

    # Delete a book by id
    def delete(self, book_id: int) -> None:
        book = self.get(book_id)

        if not book:
            raise BookNotFoundError(book_id)

        try:
            self.db.delete(book)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise SQLAlchemyError(book_id) from e

    # Find a book(books) using title, author and/or year
    def search(
        self,
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
    ) -> list[Book]:
        final_query = self.db.query(Book)

        filters = []

        if title is not None and title != "":
            filters.append(Book.title.ilike(f"%{title}%"))
        if author is not None and author != "":
            filters.append(Book.author.ilike(f"%{author}%"))
        if year is not None:
            filters.append(Book.year == year)

        if filters:
            final_query = final_query.filter(*filters)

        return final_query.all()
