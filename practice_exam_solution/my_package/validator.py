# Your solution for Problem 3 goes here.
import re 
def is_valid_student_id(student_id): 
    pattern = r"^S\d{5}$"

    if not re.search(pattern, student_id): 
        return False
    else: 
        return True
