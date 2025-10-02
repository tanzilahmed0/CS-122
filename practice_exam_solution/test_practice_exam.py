import unittest
import os
import sys
from io import StringIO


# --- IMPORTANT ---
# This is the INSTRUCTOR'S test file to verify the student's solution.
#
# Run tests from the `practice_exam_solution` directory:
# python -m unittest test_practice_exam.py

class TestPracticeExam(unittest.TestCase):
    """
    This class contains unit tests for the integrated CS 122 Practice Exam.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for all tests. Redirect stdout to capture print statements."""
        cls.held_stdout = sys.stdout
        sys.stdout = StringIO()
        print("--- Starting CS 122 Practice Exam Tests ---")

    @classmethod
    def tearDownClass(cls):
        """Tear down after all tests. Restore stdout."""
        sys.stdout = cls.held_stdout
        print("\n--- Finished CS 122 Practice Exam Tests ---")

    def setUp(self):
        """Clear stdout buffer before each test."""
        sys.stdout.truncate(0)
        sys.stdout.seek(0)

    def test_problem_1_student_validation(self):
        """
        Problem 1: Testing Student ID validation in the constructor.
        """
        print("\n--- Testing Problem 1: Student ID Validation ---")
        try:
            from main import Student
            # Test that a valid ID works
            try:
                Student("S12345", "Valid Student")
            except ValueError:
                self.fail("Student constructor raised ValueError for a valid ID 'S12345'.")

            # Test that invalid IDs raise ValueError
            with self.assertRaises(ValueError, msg="ValueError not raised for invalid ID 'S1234'."):
                Student("S1234", "Invalid Student")
            with self.assertRaises(ValueError, msg="ValueError not raised for invalid ID 's12345'."):
                Student("s12345", "Invalid Student")
            with self.assertRaises(ValueError, msg="ValueError not raised for invalid ID 'T12345'."):
                Student("T12345", "Invalid Student")

            print("Student ID Validation test passed.")
        except ImportError:
            self.fail("Could not import `Student` class from main.py.")
        except Exception as e:
            self.fail(f"An unexpected error occurred in Student Validation test: {e}")

    def test_problem_1_course_and_exceptions(self):
        """
        Problem 1: Testing Course capacity and CourseFullError.
        """
        print("\n--- Testing Problem 1: Course & Exceptions ---")
        try:
            from main import Student, Course, CourseFullError
            course = Course("Intro to Python", 1)
            student1 = Student("S11111", "Alice")
            student2 = Student("S22222", "Bob")

            course.add_student(student1)
            self.assertEqual(len(course.students), 1, "Student was not added to the course correctly.")

            with self.assertRaises(CourseFullError, msg="CourseFullError was not raised for a full course."):
                course.add_student(student2)

            self.assertEqual(len(course.students), 1, "A student was added to a full course.")

            print("Course & Exceptions test passed.")
        except ImportError:
            self.fail("Could not import `Student`, `Course`, or `CourseFullError` from main.py.")
        except Exception as e:
            self.fail(f"An unexpected error occurred in Course & Exceptions test: {e}")

    def test_problem_2_decorator_and_method(self):
        """
        Problem 2: Testing the @log_call decorator and get_student_names method.
        """
        print("\n--- Testing Problem 2: Decorator & Method ---")
        try:
            from main import Student, Course
            course = Course("Data Structures", 2)
            student1 = Student("S33333", "Charlie")
            course.add_student(student1)

            names = course.get_student_names()
            self.assertEqual(names, ["Charlie"], "get_student_names() did not return the correct list of names.")

            output = sys.stdout.getvalue()
            self.assertIn("[LOG] Calling function: get_student_names", output)

            print("Decorator & Method test passed.")
        except ImportError:
            self.fail("Could not import `Student` and/or `Course` classes from main.py.")
        except Exception as e:
            self.fail(f"An unexpected error occurred in Decorator & Method test: {e}")

    def test_problem_3_package_and_regex(self):
        """
        Problem 3: Testing the is_valid_student_id function.
        """
        print("\n--- Testing Problem 3: Package & Regex ---")
        try:
            from my_package.validator import is_valid_student_id
            self.assertTrue(is_valid_student_id("S12345"), "Failed on a valid ID 'S12345'.")
            self.assertFalse(is_valid_student_id("s12345"), "Failed to detect invalid case.")
            self.assertFalse(is_valid_student_id("S1234"), "Failed to detect not enough digits.")

            print("Package & Regex test passed.")
        except ImportError:
            self.fail("Could not import `is_valid_student_id` from `my_package.validator`.")
        except Exception as e:
            self.fail(f"An unexpected error occurred in Package & Regex test: {e}")


if __name__ == '__main__':
    # unittest.main() provides a command-line interface to the test script,
    # discovers the tests in this file, and runs them.
    unittest.main(verbosity=2)

