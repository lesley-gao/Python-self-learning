# Basic exception handling syntax
try:
    f = open("D:/abc.txt", "r", encoding="UTF-8")    # Initially, the file "abc.txt" didn't exist
except:
    print("An exception occurred because the file does not exist. I will change the open mode to 'w' to open the file.")
    f = open("D:/abc.txt", "w", encoding="UTF-8")


# Handling a specific exception
try:
    print(name)
except NameError as e:
    print("An exception occurred: the variable is undefined.")
    print(e)   # 'e' is the exception object, which contains the error information that would be shown if the exception were not caught.


# Handling multiple specific exceptions
try:
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("An exception occurred: either a variable is undefined or a division by zero error.")
# If the exception type is not set correctly, the exception will not be caught.


# Catching all exceptions
try:
    f = open("D:/123.txt", "r")
except Exception as e:
    print("An exception occurred.")
else:
    print("So happy, no exceptions occurred.")


# finally: code that executes regardless of whether an exception occurred or not
try:
    f = open("D:/123.txt", "r", encoding="UTF-8")
except Exception as e:
    print("An exception occurred.")
    f = open("D:/123.txt", "w", encoding="UTF-8")
else:
    print("So happy, no exceptions occurred.")
finally:
    print("I am 'finally'. I will execute whether an exception occurred or not.")
    f.close()



# exception propagation
def func1():
    print("func1 starts executing")
    num = 1 / 0    # Simulating an exception: division by zero
    print("func1 ends executing")

def func2():
    print("func2 starts executing")
    func1()
    print("func2 ends executing")

def main():
    try:
        func2()
    except Exception as e:        # exception is handled here
        print(f"An exception occurred. Exception details: {e}")

main()

# Therefore, we don't need to catch the exception at the lowest level where it actually occurs;
# we can catch it at a higher level because it will propagate upwards.