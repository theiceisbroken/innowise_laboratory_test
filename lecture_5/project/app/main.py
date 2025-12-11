from custom_exceptions.exception_handlers import (
    book_create_error_handler,
    book_not_found_handler,
    book_update_error_handler,
)
from custom_exceptions.exceptions import (
    BookNotCreatedError,
    BookNotFoundError,
    BookUpdateError,
)
from db.database import init_db
from fastapi import FastAPI
from routers.book import router as book_router

# Create the FastAPI application
app = FastAPI()

init_db()


# Include the book router inside the app
app.include_router(book_router)

# Add all of the exception handlers
app.add_exception_handler(BookNotFoundError, book_not_found_handler)
app.add_exception_handler(
    BookNotCreatedError, book_create_error_handler
)
app.add_exception_handler(BookUpdateError, book_update_error_handler)
