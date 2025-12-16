''' 1: Create grades.py.
• 2: Write a function add_grade(student, course, grade) that adds or updates the
grade for the given course in the student’s grades dictionary.
• 3: Write a function get_class_average(students) that computes the average grade
across all students and courses ''' 
from student import Student

def add_grade(student, course, grade): 
    student.grades[course] = grade 

def get_class_average(students): 
    total = 0 
    count = 0 

    for student in students: 
        total += students.grade 
        count += 1 

    return total / count