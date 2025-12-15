from datetime import datetime
class Movie: 

    def __init__(self, title, director, genre, year, rating): 
        current_year = datetime.datetime.now().year

        if not title or not isinstance(title, str): 
            raise ValueError("Invalid Title")
        
        if not director or not isinstance(director, str): 
            raise ValueError("Invalid Director")

        if not genre or not isinstance(genre, str): 
            raise ValueError("Invalid Genre")
        
        if not (1900 <= year <= current_year): 
            raise ValueError("Invalid Year")

        if not (0 <= rating <= 10.0):
            raise ValueError("Invalid Rating")

        
        
        self.title = title
        self.director = director 
        self.genre = genre
        self.year = int(year) 
        self.rating = float(rating) 


    def to_dict(self): 
        return {
            'title': self.title, 
            'director': self.director, 
            'genre': self.genre,
            'year': self.year,
            'rating': self.rating
        }