import pytest 

from book import Book 
from inventory import add_book, search_by_title

def test_valid_book(): 
    b = Book("Test Title", "Author", 2000, "Fiction", 4.5) 

    assert b.title == "Test Title"
    assert b.author == "Author"
    assert b.year == 2000
    assert b.genre == 'Fiction'
    assert b.rating == 4.5 

def test_book_invalid_title(self):
        with pytest.raises(ValueError):
            Book("", "Author", 2000, "Fiction", 4.5)

def test_book_invalid_year(self):
    with pytest.raises(ValueError):
        Book("Title", "Author", 1499, "Fiction", 4.5)

def test_add_book():
    books = []
    b = b = Book("Test Title", "Author", 2000, "Fiction", 4.5) 
    add_book(b, books)
    assert len(books) == 1 
    assert books[0] is b

def test_search_by_title():
    books = [
            Book("A", "Author", 2001, "Fiction", 4.0),
            Book("B", "Author", 2002, "Fiction", 4.1)
        ]
    results = search_by_title(2002, books)
    assert len(results) == 1
    assert results[0].title == "B"

    no_matches = search_by_title("Nonexistent Title", books)
    assert no_matches == []
