class BookNotFoundError(Exception):
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"The book with {book_id} ID not found.")


class BookNotCreatedError(Exception):
    def __init__(self, message: str = "The book was not created."):
        super().__init__(message)


class BookUpdateError(Exception):
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"The book wity {book_id} ID not updated.")
