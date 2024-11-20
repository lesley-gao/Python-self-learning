# Define a set
from data_container.list import myList

my_set = {"Python", "Java", "JavaScript", "TypeScript","Go", "C++"}
my_set_empty = set()  # Define an empty set

print(f"The content of my_set is: {my_set}, type: {type(my_set)}")
print(f"The content of my_set_empty is: {my_set_empty}, type: {type(my_set_empty)}")
#The content of my_set is: {'Go', 'Python', 'JavaScript', 'Java', 'TypeScript', 'C++'}, type: <class 'set'>
#The content of my_set_empty is: set(), type: <class 'set'>

# Add new elements
my_set.add("Python") # Duplicate elements will not be added again
my_set.add("R")
print(f"The result after adding elements to my_set is: {my_set}")
# The result after adding elements to my_set is: {'Go', 'Python', 'JavaScript', 'Java', 'R', 'TypeScript', 'C++'}

# Remove an element
my_set.remove("R")
print(f"The result after removing 'R' from my_set is: {my_set}")
# The result after removing 'R' from my_set is: {'Go', 'Python', 'JavaScript', 'Java', 'TypeScript', 'C++'}

# Randomly remove an element
my_set = {"Python", "Java", "JavaScript", "TypeScript","Go", "C++"}
element = my_set.pop()
print(f"The element removed from the set is: {element}, the set after removal: {my_set}")
# The element removed from the set is: Go, the set after removal: {'Python', 'JavaScript', 'Java', 'TypeScript', 'C++'}

# Clear the set
my_set.clear()
print(f"The result after clearing the set is: {my_set}")
# The result after clearing the set is: set()

# Find the difference of two sets
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)   # keep the content of set1 that do not exist in set2, set1 won't change
print(f"The result after finding the difference is: {set3}")
print(f"The original content of set1 after finding the difference: {set1}")
print(f"The original content of set2 after finding the difference: {set2}")
# The result after finding the difference is: {2, 3}
# The original content of set1 after finding the difference: {1, 2, 3}
# The original content of set2 after finding the difference: {1, 5, 6}

# Remove the difference of two sets
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)  # set1 will be changed
print(f"The result after removing the difference, set1: {set1}")
print(f"The result after removing the difference, set2: {set2}")
# The result after removing the difference, set1: {2, 3}
# The result after removing the difference, set2: {1, 5, 6}

# Merge two sets into one
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"The result after merging two sets: {set3}")
print(f"Content of set1 after merging: {set1}")
print(f"Content of set2 after merging: {set2}")
# The result after merging two sets: {1, 2, 3, 5, 6}
# Content of set1 after merging: {1, 2, 3}
# Content of set2 after merging: {1, 5, 6}


# Count the number of elements in the set using len()
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num = len(set1)
print(f"The number of elements in the set is: {num}")
# The number of elements in the set is: 5

""" =============================================================================== """
""" ===========================  Iterating over a set   =========================== """
""" =============================================================================== """
# Sets do not support indexing, so while loops cannot be used
# We can use for loops
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"The elements in the set include: {element}")
# The elements in the set include: 1
# The elements in the set include: 2
# The elements in the set include: 3
# The elements in the set include: 4
# The elements in the set include: 5
