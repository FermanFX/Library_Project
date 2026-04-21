import json
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

# count_call decorator
def count_call(func):#2
    """Decorator: counts function calls"""
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] Call Count: {call_count}")
        return result
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@count_call #2
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
        # self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print(f"'{self.title}' marked as read.")
    def display_info(self):
        read_status = "Read" if self.is_read else "Not Read"
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Status: {read_status}")

class Library:
    def __init__(self):
        self.books = []
    
    @count_call #2
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")
    def show_all_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Status: {'Read' if book.is_read else 'Not Read'}")
            
class Ebook(book): #4
    def __init__(self, title, author, year, is_read, genre="Unknown", filesize=0):
        super().__init__(title, author, year, is_read, genre)
        self.filesize = filesize


# book_iterator 
def book_iterator(genre_filter): #1
    for book in library:
        if book["genre"] == genre_filter:
            yield book
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {book['is_read']}")

#Used json module to save and load the library from a file
def save_library_to_json(file_name): #3
    """Saves the function library to a JSON file"""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(library, file, indent=4, ensure_ascii=False)
        print(f"Library saved to {file_name}.")
        return True
    except FileNotFoundError:
        print(f"Error: File path '{file_name}' not found.")
        return False
    except IOError as e:
        print(f"IO Error while saving: {e}")
        return False
    except TypeError as e:
        print(f"Error: Object cannot be serialized to JSON: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error saving library: {e}")
        return False

def load_library_from_json(file_name): #3
    """Load the library from a JSON file"""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            loaded_books = json.load(file)
        
        if not isinstance(loaded_books, list):
            print(f"Error: JSON file must contain a list of books.")
            return False
        
        library.clear()
        library.extend(loaded_books)
        print(f"Library loaded from {file_name}. Total books: {len(library)}")
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_name}'.")
        return False
    except IOError as e:
        print(f"IO Error while loading: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error loading library: {e}")
        return False

save_library_to_json("./data/library.json")
load_library_from_json("./data/library.json")