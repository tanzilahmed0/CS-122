from utils import log_operation, filter_by_author, book_generator

@log_operation
def add_book(library, title, author): 
    library.append({'title': title, 'author': author})

@log_operation
def remove_book(library, title):
    found = False
    for book in library:
        if book['title'] == title: 
            library.remove(book)
            found = True
            break
    if found == False: 
        print(f"Error: Book '{title}' not found.")

def list_books(library):
    if not library:
        print("The library is empty.") 
    else: 
        for book in library: 
            print(f"{book['title']} by {book['author']}")


