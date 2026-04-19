app_name = "library"
version = "0.1"
is_active = True
book_count =0 
library = []
print(f"Library app {app_name} version {version} is active: {is_active}")

def create_book(title, author, year, is_read, genre="Unknown"):

    book={
        "title": title,
        "author":author,
        "year":year,
        "is_read":is_read,
        "genre": genre
    }
    return book
def is_classic(book: dict):
    if book["year"] < 1950:
        return True
    return False

book1 = create_book("To Kill a Mockingbird", "Harper Lee", 1960, True, "Fiction")
print(is_classic(book1)) 

def book_era(book: dict):
    if book["year"] > 2000:
        return "new"
    elif book["year"] <= 1950:
        return "classic"
    return True

def add_books(book: dict)-> None:
    library.append(book)
    print(f"Added '{book['title']}' to the library {len(library)}.")

def remove_book(book_title:str)-> None:
    which_book ='aa'
    for book in library:
        if book["title"] == book_title:
            which_book = book
            library.remove(which_book)
            print(f'Book "{book_title}" removed from the library.')
            return
    print(f'Book "{book_title}" not found in the library.')

add_books(create_book("Əli və Nino", "Qurban Səid", 1937, "Roman"))
add_books(create_book("1984", "George Orwell", 1949, "Distopiya"))
add_books(create_book("Sapiens", "Yuval Noah Harari", 2011, "Tarix"))
book_id = ("ISBN-001", "Əli və Nino")
print(f"ID tuple: {book_id}")

def get_all_generes():
    genres = set()
    for book in library:
        genres.add(book["genre"])
    return genres


my_genres = {"Roman", "Tarix", "Fantastika"}
friend_genres = {"Roman", "Detektiv", "Fantastika"}
print("Ortaq:", my_genres & friend_genres)
print("Birləşmə:", my_genres | friend_genres)
print("Fərq:", my_genres - friend_genres)

#kitablarin janrlarini yazsin ve kitbalarin ili 1950-de kicikdir
classic_books = [book["title"] for book in library if book["year"] < 1950]
print(f'Classic books: {classic_books}')

authors = [book["author"] for book in library]
print(f'Authors in the library: {authors}')

year_2000 = [book["title"] for book in library if book["year"] > 2000]
print(f'Books published after 2000: {year_2000}')

class book:
    def __init__(self, title, author, year, is_read, genre="Unknown"):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = is_read
        self.genre = genre
        self.is_read = False

        def mark_as_read(self):
            self.is_read = True
            print(f"'{self.title}' marked as read.")
        def display_info(self):
            if self.is_read:
                read_status = "Read"
            else:
                read_status = "Not Read"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")
    def show_all_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Status: {'Read' if book.is_read else 'Not Read'}")
            