from datetime import datetime 

def log_calls(func): 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) 

        timestamp = datetime.now()
        with open("logs.txt", "a") as f: 
            f.write(f"{timestamp} | {func.__name__} | args={args} | kwargs={kwargs}\n" )

        return result 
    return wrapper

def validate_year(func):
    def wrapper(*args, **kwargs): 
        year = kwargs.get("year", None)

        if year is None: 
            raise ValueError("No year")

        cur_year = datetime.now().year 

        if not (1500 <= year <= cur_year): 
            raise ValueError("Enter a valid year")
        
        return func(*args, **kwargs)

    return wrapper


def filter_by_genre(books, genre):
    genre = genre.lower()
    for book in books: 
        if book.genre.lower == genre: 
            yield book 
