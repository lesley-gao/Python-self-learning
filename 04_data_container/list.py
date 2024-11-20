my_list1 = ["Tom", "Lily", "Rose"]
my_list2 = ["iloveyou", 666, True]    # can include different data types
my_list3 = [[1,2,3], [4,5,6]]         # nested list

print(my_list1[0])   # get the first element of my_list1. Result: Tom
print(my_list1[-1])  # get the last element of my_list1. Result: Rose
print(my_list1[1])   # get the second element of my_list1.Result: Lily
print(my_list1[-2])  # get the second to last element of my_list1.Result: Lily

print(my_list3[1][2]) # get a value of the nested list my_list3. Result: 6

""" =============================================================================== """
""" =============================  methods of list  =============================== """
""" =============================================================================== """
myList = ["Python", "Java", "JavaScript", "TypeScript"]

# 1.1 Find the index of an element in the list
index = myList.index("JavaScript")
print(f"The index of 'JavaScript' in the list is: {index}")

# 1.2 If the element being searched for does not exist, an error will occur
# index = myList.index("hello")
# print(f"The index of 'hello' in the list is: {index}")   # ValueError: 'hello' is not in list

# 2. Modify the value at a specific index
myList[0] = "C++"
print(f"After modifying an element by index, the list is:{myList}")

# 3. Insert a new element at a specific index
myList.insert(1, "C")
print(f"After inserting an element, the list is: {myList}")

# 4. Append a new element to the list
myList.append("Go")
print(f"After appending an element, the list is: {myList}")

# 5. Add multiple elements to the list using extend
myList2 = [1, 2, 3]
myList.extend(myList2)
print(f"After appending another list, the list is: {myList}") #['C++', 'C', 'Java', 'JavaScript', 'TypeScript', 'Go', 1, 2, 3]

# 6. Delete an element at a specific index (2 methods)
myList = ["Python", "Java", "JavaScript", "TypeScript"]

# 6.1 Method 1: del list[index]
del myList[2]
print(f"After deleting an element, the list is: {myList}")  #['Python', 'Java', 'TypeScript']

# 6.2 Method 2: list.pop(index)
myList = ["Python", "Java", "JavaScript", "TypeScript"]
element = myList.pop(2)
print(f"After using pop to remove an element, the list is: {myList}, the removed element is: {element}")

# 7. Remove the first occurrence of a specific element in the list
myList = ["Python", "Java", "JavaScript", "TypeScript", "Python"]
myList.remove("Python")
print(f"After using remove to delete an element, the list is:{myList}") #["Java", "JavaScript", "TypeScript", "Python"]

# 8. Clear the list
myList.clear()
print(f"The list has been cleared, the result is: {myList}")

# 9. Count the occurrences of a specific element in the list
myList = ["Python", "Java", "JavaScript", "TypeScript", "Python"]
count = myList.count("Python")
print(f"The number of occurrences of 'Python' in the list is: {count}")

# 10. Count the total number of elements in the list
myList = ["Python", "Java", "JavaScript", "TypeScript"]
count = len(myList)
print(f"The total number of elements in the list is: {count}")



""" =============================================================================== """
""" ===========================  Iterating over a list  =========================== """
""" =============================================================================== """
myList = ["Python", "Java", "JavaScript", "TypeScript"]

# while loop
index = 0
while index < len(myList):
    element = myList[index]
    print(element)
    index += 1

# For loop
for element in myList:
    print(element)


# practices
example_list = [1,2,3,4,5,6,7,8,9,10]
print("================== while loop ==================")
new_list = []
index = 0
while index < len(example_list):
    if example_list[index] % 2 == 0:
        new_list.append(example_list[index])
    index +=1
print(f"Use a while loop to extract the even numbers from the original list and create a new list: {new_list}")

print("================== for loop ==================")
new_list2 = []
for element in example_list:
    if element % 2 == 0:
        new_list2.append(element)
print(f"Use a for loop to extract the even numbers from the original list and create a new list: {new_list2}")