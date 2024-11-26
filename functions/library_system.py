DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        pass  # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    with open(DATABASE_FILE, 'a') as db:
        db.write(f"\n{title},{author}")


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    with open(DATABASE_FILE, "r") as db:
        lines = db.readlines()
        books_dict = {}
        for line in lines[1:]:
            line = line.strip().split(",")
            books_dict[line[0]] = line[1]
    try:
        book = {title:books_dict[title]}
        return book
    except:
        raise KeyError(f"The book you are looking for is not in the database")

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    with open(DATABASE_FILE, "r") as db:
        lines = db.readlines()
        books_dict = {}

        for line in lines[1:]:
            line = line.strip().split(",")
            books_dict[line[0]] = line[1]

        return books_dict
