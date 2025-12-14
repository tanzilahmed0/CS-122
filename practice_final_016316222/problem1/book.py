from datetime import datetime 

class Book:

    def __init__(self, title, author, year, genre, rating):  

        if not title or not isinstance(title, str): 
            raise ValueError("Title must be non empty string")
        if not author or not isinstance(author, str): 
            raise ValueError("Author must be a non empty string")
        
        if not (1500 <= year <= 2025): 
            raise ValueError("Year must be a valid year")

        if not (0.0 <= rating <= 5.0) or not isinstance(rating, float): 
            raise ValueError(" Rating must be valid")
        
        self.title = title
        self.author = author 
        self.year = year
        self.genre = genre 
        self.rating = rating 

    
    def __str__(self): 
        return f"{self.title} by {self.author} ({self.year} - {self.genre} [Rating: {self.rating}])"


    def to_csv_row(self): 
        return [self.title, self.author, self.year, self.genre, self.rating]

