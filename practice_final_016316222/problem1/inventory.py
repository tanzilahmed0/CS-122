import csv 
from book import Book

def add_book(book, books): 
    books.append(book)

def search_by_year(year, books): 
    output = []
    for i in books: 
        if i.year == year: 
            output.append(i)
    
    return output

def save_to_csv(books, path): 
    with open(path, "w", newline="") as f: 
        writer = csv.writer(f)
        writer.writerow(['title', 'author', 'year', 'genre', 'rating'])
        for book in books: 
            writer.writerow(book.to_csv_row())

def load_from_csv(path): 
    books = []

    with open(path, "r", newline="") as f: 
        reader = csv.DictReader(f)
        for row in reader: 
            book = Book(title = row['title'], author = row['author'], 
            year = row['year'], genre = row['genre'], rating = row['rating']) 
            
            books.append(book)
    
    return books
