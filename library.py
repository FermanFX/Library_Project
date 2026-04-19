app_name = "library"
version = "0.1"
is_active = True
book_count =0 

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