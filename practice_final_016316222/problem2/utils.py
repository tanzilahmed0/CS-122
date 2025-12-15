import time 
def track_time(func): 
    def wrapper(*args, **kwargs): 
        start = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start 
        with open('movie_logs.txt', 'a') as f: 
            f.write(f"{func.__name__} elapsed time was {total_time} seconds")
        
        return result
    return wrapper 


def stream_suggestions(movies): 
    for i in movies: 
        yield i