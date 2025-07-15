from book_status import BookStatus
from borrowing_activity import BorrowingActivity
class Book:
    def __init__(self, title, author, isbn_number, publication_year, availability_status:BookStatus = BookStatus.AVAILABLE):
        self.title =  title
        self.author = author
        self.isbn_number = isbn_number
        self.publication_year = publication_year
        self.availability_status = availability_status
        self.borrowing_activity : list[BorrowingActivity] = []

    def get_availability_status(self):
        return self.availability_status