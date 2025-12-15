from tokenize import generate_tokens
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker 
from book import Book

Base = declarative_base()

class BookModel(Base): 
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    rating = Column(Float)

def init_db(url='sqlite:///books.db'):
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session()

def add_book_db(book, session):
    row = BookModel(
        title = book.title,
        author = book.author,
        year=book.year,
        genre=book.genre, 
        rating=book.rating
    )
    session.add(row)
    session.commit()

def get_all_books(session): 
    # return rows (all books)
    rows = session.query(BookModel).all()
    output = []

    for r in rows: 
        output.append(Book(r.title, r.author, r.year, r.genre, r.rating))
    
    return output




