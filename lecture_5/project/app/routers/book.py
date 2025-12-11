from deps.repository import get_book_repository
from fastapi import APIRouter, Depends, HTTPException
from repositories.book_repository import BookRepositoryProtocol
from schemas.book import BookCreate, BookRead, BookUpdated

router = APIRouter(prefix="/books", tags=["Books"])


# POST "/books/" - create a new book
@router.post("/", response_model=BookRead)
async def create_book_endpoint(
    book_data: BookCreate,
    repo: BookRepositoryProtocol = Depends(get_book_repository),
):
    book = repo.create(book_data)
    return book


# GET "/books/" - get all books
@router.get("/", response_model=list[BookRead])
async def get_books_endpoint(
    repo: BookRepositoryProtocol = Depends(get_book_repository),
):
    return repo.list()


# DELETE "/books/{book_id}" - delete a book
@router.delete("/{book_id}")
async def delete_book_endpoint(
    book_id: int,
    repo: BookRepositoryProtocol = Depends(get_book_repository),
):
    repo.delete(book_id)
    return {"message": f"The book with {book_id} ID deleted."}


# PUT "/books/{book_id}" - update a book
@router.put("/{book_id}", response_model=BookRead)
async def update_book_endpoint(
    book_id: int,
    book_data: BookUpdated,
    repo: BookRepositoryProtocol = Depends(get_book_repository),
):
    result = repo.update(book_id, book_data)
    return result


# GET "/books/search/" - search for books
@router.get("/search/", response_model=list[BookRead])
async def search_books_endpoint(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    repo: BookRepositoryProtocol = Depends(get_book_repository),
):
    return repo.search(title, author, year)
