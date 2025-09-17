def log_operation(func): 
    """Decorator that logs function execution before calling the original function"""
    def wrapper(*args, **kwargs): 
        print(f"Executing {func.__name__}") 
        result = func(*args, **kwargs)
        return result
    return wrapper

# Lambda function for filtering books by author
filter_by_author = lambda library, author: [book for book in library if book['author'] == author] 

def book_generator(library): 
    """Generator that yields books one at a time"""
    for book in library: 
        yield book