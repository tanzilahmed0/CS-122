#Your solutions for Problems 1 and 2 go here.
from my_package.validator import is_valid_student_id

class CourseFullError(Exception): 
    pass 

 def log_call(func): 
        def wrapper(*args, **kwargs): 
            print(f"[LOG] Calling function {func.__name__}")

            return func(*args, **kwargs) 

        return wrapper

class Student:
    def __init__(self, student_id, name): 
        if not is_valid_student_id(student_id): 
            raise ValueError("Invalid Student Id") 
        
        self.student_id = student_id 
        self.name = name 


class Course: 
    def __init__(self, course_name, capacity): 
        self.course_name = course_name
        self.capacity = capacity
        self.students = []

    def add_student(self, student): 
        if len(self.students) + 1 > self.capacity: 
            raise CourseFullError("Error course is full")
        
        self.students.append(student)


    @log_call
    def get_student_names(self): 
        student_list 

        for student in self.students: 
            student_list.append(student.name)
        
        return student_list


    
