from multiprocessing import Value
import unittest
from movie import Movie 
from tracker import add_movie, remove_movie, recommend_by_genre 
from db import save_movie, load_movies

class TestMovieTracker(unittest.TestCase):

    def valid_movie(self): 
        with self.assertRaises(ValueError): 
            Movie("", "Test", "Romance", 2014, 7.3)
        with self.assertRaises(ValueError): 
            Movie("Name", "", "Romance", 2014, 7.3)
        with self.assertRaises(ValueError): 
            Movie("Name", "Test", "", 2014, 7.3)
        with self.assertRaises(ValueError): 
            Movie("Name", "Test", "Romance", 1700, 7.3)
        with self.assertRaises(ValueError): 
            Movie("Name", "Test", "Romance", 2014, 19.2)
        
        m = Movie("Name", "Test", "SciRomance-Fi", 2014, 7.3)
        self.assertEqual(m.title, "Name")

    
    def test_add_remove_movie(self):
        tracker = MovieTracker()
        m = Movie("Inception", "Nolan", "Sci-Fi", 2010, 9.0)
        tracker.add_movie(m)
        self.assertEqual(len(tracker.movies), 1)
        self.assertTrue(tracker.remove_movie("Inception", 2010))
        self.assertFalse(tracker.remove_movie("Matrix", 1999))

    def test_recommend_by_genre(self):
        tracker = MovieTracker()
        tracker.add_movie(Movie("A", "Dir1", "Drama", 2000, 7.0))
        tracker.add_movie(Movie("B", "Dir2", "Drama", 2005, 8.5))
        tracker.add_movie(Movie("C", "Dir3", "Action", 2010, 9.0))

        recs = tracker.recommend_by_genre("Drama", 7.5)
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0].title, "B")

    def test_db_integration(self):
        session = setup_db()
        m = Movie("TestMovie", "TestDir", "TestGenre", 2020, 7.5)
        save_movie(m, session)
        movies = load_movies(session)
        self.assertTrue(any(movie.title == "TestMovie" for movie in movies))

if __name__ == '__main__':
    unittest.main()