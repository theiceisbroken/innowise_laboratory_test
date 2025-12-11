from custom_exceptions.exceptions import (
    BookNotCreatedError,
    BookNotFoundError,
    BookUpdateError,
)
from fastapi import Request, status
from fastapi.responses import JSONResponse


async def book_not_found_handler(request: Request, exc: Exception):
    assert isinstance(exc, BookNotFoundError)
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )


async def book_create_error_handler(request: Request, exc: Exception):
    assert isinstance(exc, BookNotCreatedError)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)},
    )


async def book_update_error_handler(request: Request, exc: Exception):
    assert isinstance(exc, BookUpdateError)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": str(exc)},
    )
