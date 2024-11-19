# Using import to import the time module
import time        # Import the built-in Python time module (time.py file)
print("Hello")     # Output "Hello"
time.sleep(5)      # Use . to call all functions (classes, functions, variables) inside the module
print("I am fine") # Output "I am fine"

# Using from to import the sleep function from the time module
from time import sleep
print("Hello")     # Output "Hello"
sleep(5)           # Call the sleep function to pause the program for 5 seconds
print("I am fine") # Output "I am fine"

# Using * to import all functions from the time module
from time import *       # * means everything
print("Hello")
sleep(5)
print("I am fine")

# Using "as" to give an alias to a specific module
import time as t
print("Hello")
t.sleep(5)
print("I am fine")

# Using "as" to give an alias to a specific function
from time import sleep as sl
print("Hello")
sl(5)
print("I am fine")
