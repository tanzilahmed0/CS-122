''' 1: Create student.py.
• 2: Define a class Student with name, student_id, and grades (a dictionary mapping
course names to numeric grades).
• 3: In the constructor, verify name and student_id are non-empty strings and grades
mapping is non-empty; raise ValueError for violations.
• 4: Implement a method average_grade that computes and returns the mean of all course
grades ''' 

class Student: 
    
    def __init__(self, name, student_id, grades): 

        if not name or not isinstance(name, str): 
            raise ValueError("Enter Valid Name") 
        if not student_id or not isinstance(student_id, str): 
            raise ValueError("Enter Valid Student ID")
        if not grades: 
            raise ValueError("Enter Valid Grades")
        
        self.name = name
        self.student_id = student_id 
        self.grades = grades 

    def average_grade(self): 
        total = sum.self.grades.values()
        length = len(self.grades)
        return total / length