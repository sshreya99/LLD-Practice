from book import Book
class LibraryManagementSystem:
    _instance = None
    def __init__(self):
        if LibraryManagementSystem._instance is not None:
            raise Exception("Library Management System is sigleton and can not be created twice")
        LibraryManagementSystem._instance = self
        self.books: list[Book] = []

    @staticmethod      
    def get_instance():
        if LibraryManagementSystem._instance is None:
            LibraryManagementSystem()
        return LibraryManagementSystem._instance
    
    def add_book(self):
        return True
    
    def remove_book(self):
        return True
    
    def update_book(self):
        return True
    
    def get_history_of_book(self): # borrowing activity
        return True

    def borrow_book(self):
        return True
    
    def return_book(self):
        return True