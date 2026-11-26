class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def get_status(self):
        return "Available" if self.is_available else "Issued"


class Library:
    def __init__(self):
        self.books = []

    def _find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_book(self, book):
        if self._find_book(book.book_id) is not None:
            print("Error: Book ID already exists!")
            return
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("========== BOOK LIST ==========")
        for index, book in enumerate(self.books):
            print(f"\nBook ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {book.get_status()}")
            if index < len(self.books) - 1:
                print("\n-------------------------------")

    def search_book(self, book_id):
        book = self._find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return None

        print("Book Found!")
        print(f"\nBook ID: {book.book_id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Status: {book.get_status()}")
        return book

    def issue_book(self, book_id):
        book = self._find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return

        if not book.is_available:
            print("Sorry! This book is already issued.")
            return

        book.is_available = False
        print("Book issued successfully!")

    def return_book(self, book_id):
        book = self._find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return

        if book.is_available:
            print("Sorry! This book is not currently issued.")
            return

        book.is_available = True
        print("Book returned successfully!")


def get_valid_book_id():
    while True:
        try:
            return int(input("Enter Book ID: "))
        except ValueError:
            print("Invalid input! Please enter a numeric Book ID.")


def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("\n1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            book_id = get_valid_book_id()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if not title or not author:
                print("Error: Book title and author name cannot be empty!")
                continue

            new_book = Book(book_id, title, author)
            library.add_book(new_book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = get_valid_book_id()
            library.search_book(book_id)

        elif choice == "4":
            book_id = get_valid_book_id()
            library.issue_book(book_id)

        elif choice == "5":
            book_id = get_valid_book_id()
            library.return_book(book_id)

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
