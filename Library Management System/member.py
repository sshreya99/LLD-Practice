from borrowing_activity import BorrowingActivity
from book import Book
class Member:
    def __init__(self,name,member_id,contact,borrowing_history):
        self.name = name
        self.member_id = member_id
        self.contact = contact
        self.borrowed_books = list[Book] = []
        self.borrowing_history : list[BorrowingActivity] = []