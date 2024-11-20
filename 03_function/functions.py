
"""
return multi values
"""
def example_func():
    return 1, "hi", 4.5

x, y, z = example_func()
print(x)   # 1
print(y)   # hi
print(z)   # 4.5


"""
Demonstration of various ways to pass arguments
"""

def user_info(name, age, gender):
    print(f"Name: {name}, Age: {age}, Gender: {gender}")

# Positional arguments - pass arguments in order
user_info("Leo", 20, "Male")

# Keyword arguments
user_info(name="Leo", age=11, gender="Female")
user_info(age=10, gender="Female", name="Wong")  # Keyword arguments can be passed out of order
user_info("Tian", gender="Female", age=9)

# Variable-length - Positional variable-length, *args
def user_info(*args):
    print(f"Type of args: {type(args)}, Content: {args}")

user_info(1, 2, 3, "Leo", "Male")

# Variable-length - Keyword variable-length, **kwargs
def user_info(**kwargs):
    print(f"Type of kwargs: {type(kwargs)}, Content: {kwargs}")

user_info(name="Leo", age=11, gender="Boy", addr="Beijing")




"""
Passing a function as an argument
"""

# Define a function and pass another function as an argument
def test_func(calculate):
    result = calculate(1, 2)  # Assume compute is a function
    print(f"The type of compute is: {type(calculate)}")   # The type of compute is: <class 'function'>
    print(f"The calculation result is: {result}")         # The calculation result is: 3

# Define a function that will be passed into another function
def calculate(x, y):
    return x + y

# Call test_func and pass compute
test_func(calculate)


"""
Lambda anonymous functions
"""

# Define a function and pass another function as an argument
def test_func(compute):
    result = compute(1, 2)
    print(f"The result is: {result}")

# Use lambda to pass an anonymous function
test_func(lambda x, y: x + y)    # The result is: 3