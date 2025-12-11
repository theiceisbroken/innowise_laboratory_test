from typing import Protocol

from models.book import Book
from schemas.book import BookCreate, BookUpdated


class BookRepositoryProtocol(Protocol):
    def get(self, book_id: int) -> Book | None: ...
    def list(self) -> list[Book]: ...
    def create(self, data: BookCreate) -> Book: ...
    def update(
        self, book_id: int, data: BookUpdated
    ) -> Book | None: ...
    def delete(self, book_id: int) -> bool: ...
    def search(
        self,
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
    ) -> list[Book]: ...
