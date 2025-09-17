def log_operation(func): 
    def wrapper(*args, **kwargs): 
        print(f"Executing {func.__name__}") 
        result = func(*args, **kwargs)
        return result
    return wrapper


filter_by_author = lambda library, author: [book for book in library if book['author'] == author] 

def book_generator(library): 
    for book in library: 
        yield book