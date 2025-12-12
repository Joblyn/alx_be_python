class Book:
    """
    Base class representing a book with title and author.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"
    
    def __repr__(self):
        """Return official string representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}')"

class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size attribute.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size of the ebook in KB
        """
        super().__init__(title, author)  # Call parent class constructor
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
      
    def __repr__(self):
        """Return official string representation of the ebook."""
        return f"EBook(title='{self.title}', author='{self.author}', file_size={self.file_size})"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page_count attribute.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        super().__init__(title, author)  # Call parent class constructor
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
      
    def __repr__(self):
        """Return official string representation of the print book."""
        return f"PrintBook(title='{self.title}', author='{self.author}', page_count={self.page_count})"


class Library:
    """
    A class representing a library that manages a collection of books.
    Demonstrates composition by containing Book objects.
    """
    
    def __init__(self):
        """
        Initialize a Library instance with an empty collection of books.
        """
        self.books = []  # List to store Book, EBook, and PrintBook instances
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        """
        for book in self.books:
            print(book)