# Your solutions for Problems 1 and 2 go here.
import 
# Your solutions for Problems 1 and 2 go here.
class CourseFullError(Exception): 
    pass 

class Student: 
    def __init__(self, student_id, name): 
        if not is_valid_student_id(student_id): 
            raise ValueError("Not Valid Student ID")

        self.student_id = student_id 
        self.name = name 

class Course: 
    def __init__(self, course_name, capacity): 
        self.students = [] 
        self.course_name = course_name 
        self.capacity = capacity 

    def add_student(self, student): 
        if len(self.students) + 1 > self.capacity: 
            raise CourseFullError("Course is full")
        
        else: 
            self.students.append(student)

    @log_call
    def get_student_names(self):
        student_list = []

        for i in self.students: 
            student_list.append(i) 

        return student_list


def log_call(func): 
    def wrapper(*args, **kwargs): 
        print(f"[LOG] Calling function {func.__name__}")

        return func(*args, **kwargs) 

    return wrapper



