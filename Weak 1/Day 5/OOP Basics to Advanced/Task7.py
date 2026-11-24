class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(f"Added: {title}")

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f"Removed: {title}")
        else:
            print(f"Book '{title}' not found.")

    def list_books(self):
        print("Books in Library:", self.__books)

lib = Library()
lib.add_book("Clean Code")
lib.add_book("Atomic Habits")
lib.list_books()
lib.remove_book("Clean Code")
lib.list_books()