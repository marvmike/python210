class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been lent to {member.name}")
        else:
            print(f"Sorry, {book.title} is not available for lending")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book.title}")

if __name__ == "__main__":
    # Example usage:
    # Create books
    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    # Create members
    member1 = Member("John", 101)
    member2 = Member("Alice", 102)

    # Create library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Register members
    library.register_member(member1)
    library.register_member(member2)

    # Test lending and returning books
    library.lend_book(book1, member1)
    library.lend_book(book2, member2)
    library.return_book(book1, member1)
    library.return_book(book2, member1)  # This should fail as book2 is not borrowed by member1