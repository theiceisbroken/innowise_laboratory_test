from datetime import datetime

from pydantic import BaseModel, Field, field_validator

# Define current year
CURRENT_YEAR = datetime.now().year


# Define shared fields
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int | None = Field(default=None, le=CURRENT_YEAR, ge=1)

    @field_validator("title", "author")
    def strip_spaces(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be empty.")
        return value


# Used if an user creates a book
class BookCreate(BookBase):
    pass


# Used for server response
class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True


# Used for parteal update
class BookUpdated(BaseModel):
    title: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    author: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    year: int | None = Field(default=None, le=CURRENT_YEAR, ge=1)

    class Config:
        extra = "forbid"
