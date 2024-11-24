class Student:
    def __init__(self, name, age):
        self.name = name           # 学生姓名
        self.age = age             # 学生年龄

    # __str__ magic method
    def __str__(self):
        return f"Info of this student: name:{self.name}, age:{self.age}"

    # __lt__ magic method
    def __lt__(self, other):
        return self.age < other.age   # check whether current student is younger than the other student

    # __le__ magic method
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ magic method
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("Jay", 22)
stu2 = Student("Jeff", 22)
print(stu1)            # Info of this student: name:Jay, age:31
print(str(stu2))       # Info of this student: name:Jeff, age:22
print(stu1 < stu2)     # False
print(stu1 <= stu2)    # True
print(stu1 == stu2)    # True