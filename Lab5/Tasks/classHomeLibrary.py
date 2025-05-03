class Book:
    """
    Represents a book with attributes such as ID, title, author, year, and genre.
    """
    def __init__(self, book_id, title, author, year, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"
    
    def __del__(self):
        try:
            print(f"Book '{self.title}' by {self.author} has been deleted.")
        except AttributeError:
            pass  # Ignore if attributes are already gone during cleanup

class HomeLibrary:
    """
    Represents a home library with book management functionality.
    """
    def __init__(self):
        self.books = []
        self.book_counter = 0
        self.genres = {
            "1": "Fiction",
            "2": "Non-Fiction",
            "3": "Science",
            "4": "History",
            "5": "Fantasy",
            "6": "Biography",
            "7": "Romance",
            "8": "Thriller",
            "9": "Horror",
            "0": "Other"
        }
    
    def add_book(self):
        """
        Adds a new book to the library.
        Returns: None
        """
        book_id = self.book_counter
        self.book_counter += 1

        while True:
            title = input("Enter book title: ")
            if title:
                break
            print("Book title cannot be empty.")

        while True:
            author = input("Enter author name: ")
            if author:
                break
            print("Author name cannot be empty.")

        while True:
            year = input("Enter publication year: ")
            if year.isdigit() and 1800 <= int(year) <= 2025:
                break
            print("Invalid year. Please enter a valid year between 1800 and 2025.")

        while True:
            print("Choose genre:")
            for key, value in self.genres.items():
                print(f"{key}: {value}")
            choice = input("Enter genre: ")
            if choice in self.genres:
                genre = self.genres[choice]
                break
            print("Invalid genre. Please try again.")

        book = Book(book_id, title, author, year, genre)
        self.books.append(book)
        print(f"Book ID {book_id}: '{book.title}' by {book.author} has been added.")
    
    def delete_book(self, book_id):
        """
        Deletes a book from the library by book ID.
        Returns: None
        """
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return
        print(f"Book {book_id} not found.")
    
    def find_book(self):
        """
        Finds a book in the library based on user input.
        Returns: None
        """
        try:
            found_books = self.books
            book_id = input("Enter book ID (or press Enter to skip): ")
            if book_id:
                book_id = int(book_id)
                found_books = [book for book in found_books if book.book_id == book_id]
            else:
                author = input("Enter author name (or press Enter to skip): ")
                year = input("Enter year (or press Enter to skip): ")
                genre = input("Enter genre (or press Enter to skip): ")

                if author: found_books = [book for book in found_books if book.author == author]
                if year: found_books = [book for book in found_books if book.year == year]
                if genre: found_books = [book for book in found_books if book.genre == genre]

            # Вывод результата
            if found_books:
                print("Found books:")
                for book in found_books:
                    print(book)
            else:
                print("No books found with the given criteria.")
        except ValueError:
            print("Invalid book ID. Please enter a valid number.")

    def show_menu(self):
        """
        Displays the home library menu and handles user input for book management.
        Returns: None
        """
        while True:
            print("\n1 -> Add book")
            print("2 -> Find book")
            print("3 -> Delete book")
            print("0 -> Back to main menu")
            
            match input("Enter your choice: "):
                case "1": self.add_book()
                case "2": self.find_book()
                case "3": 
                    book_id = int(input("Enter book ID to delete: "))
                    self.delete_book(book_id)
                case "0": return
                case _: print("Invalid choice. Please try again.")

