import unittest
import io
import sys
from unittest.mock import patch


# --- Custom Test Runner for Verbose, Clean Output ---

class CustomTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)
        self.stream.write(f"    [ RUNNING ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(f"    [  PASS   ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write(f"    [  FAIL   ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(f"    [  ERROR  ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


# --- End of Custom Test Runner ---


# IMPORTANT: This allows the test runner to find your code.
sys.path.insert(0, './')

try:
    from question_1.library import add_book, remove_book, list_books
    from question_1.utils import filter_by_author, book_generator
    from question_2.pricing import apply_tax, apply_discount, price_generator
except ImportError as e:
    print(f"ERROR: Could not import files. Make sure your directory structure is correct.")
    print(f"  - Details: {e}")


    # Define dummy functions to prevent further errors during test collection.
    def add_book(*args):
        pass


    def remove_book(*args):
        pass


    def list_books(*args):
        pass


    def filter_by_author(*args):
        return []


    def book_generator(*args):
        yield from []


    def apply_tax(p):
        return p


    def apply_discount(f):
        return f


    def price_generator(*args):
        yield from []


class TestLibraryManagement(unittest.TestCase):
    """Tests for Question 1: Library Management System"""

    def setUp(self):
        """Set up a fresh library for each test."""
        self.library = []

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_01_add_and_list_books(self, mock_stdout):
        """Q1: Should add books and list them correctly"""
        add_book(self.library, "1984", "George Orwell")
        add_book(self.library, "Animal Farm", "George Orwell")
        self.assertEqual(len(self.library), 2)
        self.assertEqual(self.library[0]['title'], "1984")
        list_books(self.library)
        output = mock_stdout.getvalue()
        self.assertIn("1984 by George Orwell", output)
        self.assertIn("Animal Farm by George Orwell", output)

    def test_02_remove_book(self):
        """Q1: Should remove a book by its title"""
        add_book(self.library, "1984", "George Orwell")
        remove_book(self.library, "1984")
        self.assertEqual(len(self.library), 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_03_remove_nonexistent_book(self, mock_stdout):
        """Q1: Should print an error for a non-existent book"""
        add_book(self.library, "1984", "George Orwell")
        remove_book(self.library, "Dune")
        self.assertEqual(len(self.library), 1)
        self.assertIn("Error: Book 'Dune' not found.", mock_stdout.getvalue())

    def test_04_filter_by_author(self):
        """Q1: Should filter books by a given author"""
        add_book(self.library, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
        add_book(self.library, "1984", "George Orwell")
        add_book(self.library, "Animal Farm", "George Orwell")
        orwell_books = filter_by_author(self.library, "George Orwell")
        self.assertEqual(len(orwell_books), 2)
        self.assertTrue(any(b['title'] == '1984' for b in orwell_books))

    def test_05_book_generator(self):
        """Q1: Generator should yield books one by one"""
        add_book(self.library, "Book 1", "Author A")
        add_book(self.library, "Book 2", "Author B")
        gen = book_generator(self.library)
        self.assertEqual(next(gen)['title'], "Book 1")
        self.assertEqual(next(gen)['title'], "Book 2")
        with self.assertRaises(StopIteration):
            next(gen)

    def test_06_filter_by_nonexistent_author(self):
        """Q1: Should return an empty list for an unknown author"""
        add_book(self.library, "1984", "George Orwell")
        results = filter_by_author(self.library, "Jane Austen")
        self.assertEqual(len(results), 0)


class TestEcommercePricing(unittest.TestCase):
    """Tests for Question 2: E-commerce Price Calculator"""

    def setUp(self):
        """Define the decorated function for use in tests."""

        @apply_discount
        def calculate_final_price(price):
            return apply_tax(price)

        self.calculate_final_price = calculate_final_price

    def test_01_price_below_discount_threshold(self):
        """Q2: Should apply only tax for price <= $100"""
        self.assertAlmostEqual(self.calculate_final_price(50.0), 54.0)
        self.assertAlmostEqual(self.calculate_final_price(100.0), 108.0)

    def test_02_price_above_discount_threshold(self):
        """Q2: Should apply discount then tax for price > $100"""
        self.assertAlmostEqual(self.calculate_final_price(120.0), 116.64)

    def test_03_price_generator(self):
        """Q2: Generator should yield correctly processed prices"""
        prices = [50.0, 120.0, 95.5, 210.75]
        expected = [54.0, 116.64, 103.14, 204.849]
        gen = price_generator(prices, self.calculate_final_price)
        results = list(gen)
        for i, res in enumerate(results):
            self.assertAlmostEqual(res, expected[i])

    def test_04_zero_price(self):
        """Q2: Should correctly handle a price of zero"""
        self.assertAlmostEqual(self.calculate_final_price(0.0), 0.0)


if __name__ == '__main__':
    print("=====================================")
    print("  RUNNING HOMEWORK 2 UNIT TESTS")
    print("=====================================")
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLibraryManagement))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEcommercePricing))

    runner = CustomTestRunner(verbosity=0)  # Verbosity is handled by our custom class
    result = runner.run(suite)

    print("------------------------------------")
    if result.wasSuccessful():
        print("All tests passed successfully! Great job!")
    else:
        print("Some tests failed. Please review the output above.")

