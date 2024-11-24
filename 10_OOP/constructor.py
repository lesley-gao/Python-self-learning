"""
Pratice: Ask for 10 students' names, ages, and addresses first,
print the information of each student,
and give the summary in the end.
"""
class Student:
    name = None
    age = None
    addr = None

    # Using __init__ for Python constructor
    # The constructor method is also a method, need to include `self` in the parameter list.
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Address: {self.addr}"


students = []
for i in range(1, 11):
    print(f"Currently entering information for student {i}, total of 10 students to be entered.")
    name = input("Please enter the student's name: ")
    age = input("Please enter the student's age: ")
    addr = input("Please enter the student's address: ")
    student = Student(name, age, addr)
    students.append(student)
    print(f"Student {i} information entry completed. Information: {str(student)}")

print("All student information entry completed. Details are as follows:")
for student in students:
    print(student)

