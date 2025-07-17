class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {self.status}")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_details(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Borrowed Books: {', '.join(self.borrowed_books)}")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn):
        if isbn not in self.books:
            self.books[isbn] = Book(title, author, isbn)
            print(f"Book '{title}' added successfully.")
        else:
            print("Book with same ISBN already exists.")

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
            print(f"Member '{name}' added successfully.")
        else:
            print("Member ID already exists.")

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)
        if member and book and book.status == "Available":
            book.status = "Borrowed"
            member.borrowed_books.append(book.title)
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print("Book not available or member not found.")

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)
        if member and book and book.status == "Borrowed" and book.title in member.borrowed_books:
            book.status = "Available"
            member.borrowed_books.remove(book.title)
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("Book not borrowed or member not found.")

    def display_books(self):
        for book in self.books.values():
            book.display_details()
            print()

    def display_members(self):
        for member in self.members.values():
            member.display_details()
            print()

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == "2":
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            library.add_member(member_id, name)
        elif choice == "3":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.borrow_book(member_id, isbn)
        elif choice == "4":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.return_book(member_id, isbn)
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            library.display_members()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
