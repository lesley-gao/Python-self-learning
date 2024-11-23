"""
An example of sorting a list based on a specific rule
"""
my_list = [["a", 33], ["b", 55], ["c", 11]]

# Define a function to choose the sorting key
# This function takes an element (a list) and returns the second value in the list (element[1])
def choose_sorting_key(element):
    return element[1]

# Sort the list using the custom function as the sorting key
# Sort in descending order by setting reverse=True
my_list.sort(key=choose_sorting_key, reverse=True)

print(my_list)  # Output: [['b', 55], ['a', 33], ['c', 11]]

# Option 2: using lambda
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)  # Output: [['b', 55], ['a', 33], ['c', 11]]
