# A very simple function to get the length of a string
def str_length(data):
    length = 0
    for i in data:
        length +=1
    print(f"The length of the string is {length}")

str_length("hello world")
str_length("Do you love Python?")


# A function that returns a value
def add(a, b):
    return a+b

result = add(10, 20)
print(result)


"""If a function doesn't explicitly return a value (i.e., it lacks a return statement), it will implicitly return None. 
None can be used in conditional statements to check if a variable has a meaningful value. 
For example：
if value is None:
    print("The value is empty or uninitialized.")
"""
def sayhi():
    print("Hello!")
result = sayhi();
print(f"The return value of sayhi() is {result}") # The return value of sayhi() is None
print(f"The data type of the return value is {type(result)}") # The data type of the return value is <class 'NoneType'>


# Using "global" keyword to modify the global variable inside a function
num = 100
def print_num():
    print(num)
def print_again():
    global num   # Declares that we are using the global variable num
    num = 500
    print(num)
print_num()
print_again()
print(num)