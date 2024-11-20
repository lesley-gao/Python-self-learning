# Demonstrating common functionalities of containers
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len number of elements
print(f"The number of elements in the list is: {len(my_list)}")
print(f"The number of elements in the tuple is: {len(my_tuple)}")
print(f"The number of elements in the string is: {len(my_str)}")
print(f"The number of elements in the set is: {len(my_set)}")
print(f"The number of elements in the dictionary is: {len(my_dict)}")
# The number of elements in the list is: 5
# The number of elements in the tuple is: 5
# The number of elements in the string is: 7
# The number of elements in the set is: 5
# The number of elements in the dictionary is: 5

# max maximum element
print(f"The maximum element in the list is: {max(my_list)}")
print(f"The maximum element in the tuple is: {max(my_tuple)}")
print(f"The maximum element in the string is: {max(my_str)}")
print(f"The maximum element in the set is: {max(my_set)}")
print(f"The maximum key in the dictionary is: {max(my_dict)}")
# The maximum element in the list is: 5
# The maximum element in the tuple is: 5
# The maximum element in the string is: g
# The maximum element in the set is: 5
# The maximum key in the dictionary is: key5


# min minimum element
print(f"The minimum element in the list is: {min(my_list)}")
print(f"The minimum element in the tuple is: {min(my_tuple)}")
print(f"The minimum element in the string is: {min(my_str)}")
print(f"The minimum element in the set is: {min(my_set)}")
print(f"The minimum key in the dictionary is: {min(my_dict)}")
# The minimum element in the list is: 1
# The minimum element in the tuple is: 1
# The minimum element in the string is: a
# The minimum element in the set is: 1
# The minimum key in the dictionary is: key1


# Type conversion: Container to list
print(f"The result of converting a list to a list is: {list(my_list)}")
print(f"The result of converting a tuple to a list is: {list(my_tuple)}")
print(f"The result of converting a string to a list is: {list(my_str)}")
print(f"The result of converting a set to a list is: {list(my_set)}")
print(f"The result of converting a dictionary to a list is: {list(my_dict)}")
# The result of converting a list to a list is: [1, 2, 3, 4, 5]
# The result of converting a tuple to a list is: [1, 2, 3, 4, 5]
# The result of converting a string to a list is: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# The result of converting a set to a list is: [1, 2, 3, 4, 5]
# The result of converting a dictionary to a list is: ['key1', 'key2', 'key3', 'key4', 'key5']


# Type conversion: Container to tuple
print(f"The result of converting a list to a tuple is: {tuple(my_list)}")
print(f"The result of converting a tuple to a tuple is: {tuple(my_tuple)}")
print(f"The result of converting a string to a tuple is: {tuple(my_str)}")
print(f"The result of converting a set to a tuple is: {tuple(my_set)}")
print(f"The result of converting a dictionary to a tuple is: {tuple(my_dict)}")
# The result of converting a list to a tuple is: (1, 2, 3, 4, 5)
# The result of converting a tuple to a tuple is: (1, 2, 3, 4, 5)
# The result of converting a string to a tuple is: ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# The result of converting a set to a tuple is: (1, 2, 3, 4, 5)
# The result of converting a dictionary to a tuple is: ('key1', 'key2', 'key3', 'key4', 'key5')


# Type conversion: Container to string
print(f"The result of converting a list to a string is: {str(my_list)}")
print(f"The result of converting a tuple to a string is: {str(my_tuple)}")
print(f"The result of converting a string to a string is: {str(my_str)}")
print(f"The result of converting a set to a string is: {str(my_set)}")
print(f"The result of converting a dictionary to a string is: {str(my_dict)}")
# The result of converting a list to a string is: [1, 2, 3, 4, 5]
# The result of converting a tuple to a string is: (1, 2, 3, 4, 5)
# The result of converting a string to a string is: abcdefg
# The result of converting a set to a string is: {1, 2, 3, 4, 5}
# The result of converting a dictionary to a string is: {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}


# Type conversion: Container to set
print(f"The result of converting a list to a set is: {set(my_list)}")
print(f"The result of converting a tuple to a set is: {set(my_tuple)}")
print(f"The result of converting a string to a set is: {set(my_str)}")
print(f"The result of converting a set to a set is: {set(my_set)}")
print(f"The result of converting a dictionary to a set is: {set(my_dict)}")
# The result of converting a list to a set is: {1, 2, 3, 4, 5}
# The result of converting a tuple to a set is: {1, 2, 3, 4, 5}
# The result of converting a string to a set is: {'g', 'd', 'b', 'c', 'a', 'f', 'e'}
# The result of converting a set to a set is: {1, 2, 3, 4, 5}
# The result of converting a dictionary to a set is: {'key2', 'key3', 'key4', 'key1', 'key5'}


"""
Sorting containers
Regardless of the type of container (e.g., list, tuple, string, set, or dictionary),
the result is always returned as a list."""
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"The sorting result of the list is: {sorted(my_list)}")
print(f"The sorting result of the tuple is: {sorted(my_tuple)}")
print(f"The sorting result of the string is: {sorted(my_str)}")
print(f"The sorting result of the set is: {sorted(my_set)}")
print(f"The sorting result of the dictionary keys is: {sorted(my_dict)}")
# The sorting result of the list is: [1, 2, 3, 4, 5]
# The sorting result of the tuple is: [1, 2, 3, 4, 5]
# The sorting result of the string is: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# The sorting result of the set is: [1, 2, 3, 4, 5]
# The sorting result of the dictionary keys is: ['key1', 'key2', 'key3', 'key4', 'key5']

print(f"The reverse sorting result of the list is: {sorted(my_list, reverse=True)}")
print(f"The reverse sorting result of the tuple is: {sorted(my_tuple, reverse=True)}")
print(f"The reverse sorting result of the string is: {sorted(my_str, reverse=True)}")
print(f"The reverse sorting result of the set is: {sorted(my_set, reverse=True)}")
print(f"The reverse sorting result of the dictionary keys is: {sorted(my_dict, reverse=True)}")
# The reverse sorting result of the list is: [5, 4, 3, 2, 1]
# The reverse sorting result of the tuple is: [5, 4, 3, 2, 1]
# The reverse sorting result of the string is: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
# The reverse sorting result of the set is: [5, 4, 3, 2, 1]
# The reverse sorting result of the dictionary keys is: ['key5', 'key4', 'key3', 'key2', 'key1']



