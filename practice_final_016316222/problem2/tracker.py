from movie import Movie

class MovieTracker: 

    def __init__(self):
        self.movies = []

    def add_movie(self, movie): 
        self.movies.append(movie)


    def remove_movie(self, title, year): 
        for movie in self.movies: 
            if movie.title == title and movie.year == year: 
                self.movies.remove(movie)
                return True
        return False


    def recommend_by_genre(self, genre, min_rating): 
        genre = genre.lower()
        output = []

        for movie in self.movies: 
            if movie.genre.lower() == genre and movie.rating >= min_rating: 
                output.append(movie)

        return sorted(output, key=lambda m: (-m.rating, m.rating))
