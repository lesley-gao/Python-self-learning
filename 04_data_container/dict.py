# Define a dictionary
my_dict1 = {"Aria": 99, "Felix": 88, "Wills": 77}

# Define an empty dictionary
my_dict2 = {}
my_dict3 = dict()

print(f"The content of dictionary 1 is: {my_dict1}, type: {type(my_dict1)}")
print(f"The content of dictionary 2 is: {my_dict2}, type: {type(my_dict2)}")
print(f"The content of dictionary 3 is: {my_dict3}, type: {type(my_dict3)}")
#The content of dictionary 1 is: {'Aria': 99, 'Felix': 88, 'Wills': 77}, type: <class 'dict'>
# The content of dictionary 2 is: {}, type: <class 'dict'>
# The content of dictionary 3 is: {}, type: <class 'dict'>

# Define a dictionary with duplicate keys
my_dict1 = {"Aria": 99, "Felix": 88, "Wills": 77}
print(f"The content of a dictionary with duplicate keys is: {my_dict1}")

# Get value from the dictionary based on a key
my_dict1 = {"Aria": 99, "Felix": 88, "Wills": 77}

score = my_dict1["Aria"]
print(f"Aria's exam score is: {score}")

score = my_dict1["Felix"]
print(f"Felix's exam score is: {score}")
# Aria's exam score is: 99
# Felix's exam score is: 88


# Dictionaries can be nested
stu_score_dict = {
    "Wills": {
        "Chinese": 77,
        "Math": 77,
        "English": 77
    },
    "Felix": {
        "Chinese": 88,
        "Math": 86,
        "English": 55
    },
    "Aria": {
        "Chinese": 99,
        "Math": 96,
        "English": 88
    }
}
print(f"Aria's English score is: {stu_score_dict['Aria']['English']}")  # Aria's English score is: 88

""" =============================================================================== """
""" =============================  methods of dict  =============================== """
""" =============================================================================== """

my_dict = {"Chou": 99, "Lin": 88, "Chang": 77}

# Add a new element
my_dict["Bo"] = 66
print(f"The dictionary after adding a new element is: {my_dict}")
# The dictionary after adding a new element is: {'Chou': 99, 'Lin': 88, 'Chang': 77, 'Bo': 66}

# Update an element
my_dict["Chou"] = 33
print(f"The dictionary after updating an element is: {my_dict}")
# The dictionary after updating an element is: {'Chou': 33, 'Lin': 88, 'Chang': 77, 'Bo': 66}

# Remove an element
score = my_dict.pop("Chou")
print(f"An element was removed from the dictionary, result: {my_dict}, Chou's score is: {score}")
# An element was removed from the dictionary, result: {'Lin': 88, 'Chang': 77, 'Bo': 66}, Chou's score is: 33

# Clear all elements
my_dict.clear()
print(f"The dictionary has been cleared, content: {my_dict}")
# The dictionary has been cleared, content: {}

# Get all the keys, can be used to iterate through the dictionary
my_dict = {"Chou": 99, "Lin": 88, "Chang": 77}
keys = my_dict.keys()
print(f"All keys in the dictionary are: {keys}")
# All keys in the dictionary are: dict_keys(['Chou', 'Lin', 'Chang'])

# Count the number of elements in the dictionary using len() function
num = len(my_dict)
print(f"The number of elements in the dictionary is: {num}")
# The number of elements in the dictionary is: 3



""" =============================================================================== """
""" ===========================  Iterating over a dict  =========================== """
""" =============================================================================== """
# Iterate through the dictionary
# Method 1: Get all the keys first, then use all the keys to complete the iteration
my_dict = {"Chou": 99, "Lin": 88, "Chang": 77}
keys = my_dict.keys()
for key in keys:
    print(f"The key in the dictionary is: {key}")
    print(f"The value in the dictionary is: {my_dict[key]}")

# Method 2: Directly iterate over the dictionary, each iteration directly gets a key
for key in my_dict:
    print(f"The key in the dictionary is: {key}")
    print(f"The value in the dictionary is: {my_dict[key]}")



""" =============================================================================== """
""" ================================  Practice  =================================== """
""" =============================================================================== """
# Using a for loop to promote all employees with a level of 1 by 1 level and increase their salary by 1000
example_dict = {
    "Wang": {"Department": "R&D", "Salary": 3000, "Level": 1},
    "Chou": {"Department": "Marketing", "Salary": 5000, "Level": 2},
    "Lin": {"Department": "Marketing", "Salary": 6000, "Level": 3},
    "Cheung": {"Department": "R&D", "Salary": 4000, "Level": 1},
    "Lau": {"Department": "Marketing", "Salary": 6000, "Level": 2}
}

for key in example_dict:
    if example_dict[key]["Level"] == 1:
        example_dict[key]["Salary"] += 1000
        example_dict[key]["Level"] += 1

print(example_dict)
