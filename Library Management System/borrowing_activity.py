from activity import Activity
class BorrowingActivity:
    def _init_(self,date ,member_name, activity: Activity, isbn_number):
        self.activity = activity
        self.date = date
        self.member_name = member_name
        self.isbn_number = isbn_number