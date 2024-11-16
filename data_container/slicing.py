""" =============================================================================== """
""" ==================================  slicing  ================================== """
""" =============================================================================== """
# Slice the list, starting from index 1, ending at index 4 (exclusive), with a step of 1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]  # The step defaults to 1, so it can be omitted
print(f"Result 1: {result1}")   # Result 1: [1, 2, 3]

# Slice the tuple, starting from the beginning to the end, with a step of 1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # Leaving start and end empty selects the entire tuple, and the step can be omitted
print(f"Result 2: {result2}")   # Result 2: (0, 1, 2, 3, 4, 5, 6)

# Slice the string, starting from the beginning to the end, with a step of 2
my_str = "01234567"
result3 = my_str[::2]
print(f"Result 3: {result3}")    # Result 3: 0246

# Slice the string, starting from the beginning to the end, with a step of -1
my_str = "01234567"
result4 = my_str[::-1]  # Equivalent to reversing the sequence
print(f"Result 4: {result4}")    # Result 4: 76543210

# Slice the list, starting from index 3, ending at index 1 (exclusive), with a step of -1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"Result 5: {result5}")     # Result 5: [3, 2]

# Slice the tuple, starting from the beginning to the end, with a step of -2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"Result 6: {result6}")      # Result 6: (6, 4, 2, 0)

