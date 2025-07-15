from library_management_system import LibraryManagementSystem
class Demo:
    def run():
        LibrarySystem = LibraryManagementSystem.get_instance()
        LibrarySystem.add_book()
        LibrarySystem.remove_book()
        LibrarySystem.update_book()
        LibrarySystem.get_history_of_book()
        LibrarySystem.borrow_book()
        LibrarySystem.return_book()
        

if __name__== "__main__":
    Demo().run()