from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship 
from movie import Movie


Base = declarative_base()

class MovieModel(Base): 
    __tablename__ = 'movies'
    title = Column(String, primary_key = True)
    director = Column(String)
    genre = Column(String)
    year = Column(Integer)
    rating = Column(Float)

def setup_db(): 
    engine = create_engine('sqlite:///movies.db')
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    return Session()

def save_movie(movie, session): 
    m = MovieModel(
        title = movie.title, 
        director = movie.director, 
        genre = movie.genre, 
        year = movie.year, 
        rating = movie.rating
    )

    session.add(m)
    session.commit()

def load_movies(session): 
    rows = session.query(MovieModel).all()
    output = []

    for r in rows: 
        output.append(Movie(r.title, r.director, r.genre, r.year, r.rating))
    
    return output