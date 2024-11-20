""" =============================================================================== """
""" ===================================  tuple basics  ============================ """
""" =============================================================================== """
tuple1 = (1, 'Hello', True)
tuple2 = ('Hello', )  # Note: A comma is required, otherwise it is not a tuple
tuple3 = ((1, 2, 3), (4, 5, 6))  # Tuples also support nesting, to get an element: print(t1[0][0])


""" =============================================================================== """
""" ================================= methods of tuples  ========================== """
""" =============================================================================== """
# index()
tuple4 = ("Python", "Java", "JavaScript", "TypeScript")
index = tuple4.index("Java")
print(index)    # 1

#count()
tuple5 = ("Python", "Java", "JavaScript", "TypeScript", "Python")
num = tuple5.count("Python")
print(num)   #2

#len()
tuple6 = ("Python", "Java", "JavaScript", "TypeScript", "C++")
print(f"The length of tuple 6 is {len(tuple6)}")   #The length of tuple 6 is 5

# A tuple is immutable,
# however, if it contains mutable objects (e.g., a list), the content of those mutable objects can be modified.
# For example, you can change, add, delete, or reverse the elements in the list.

# tuple6[5] = "newValue"   # will get TypeError: 'tuple' object does not support item assignment
tuple7  = ("Python", "Java", "JavaScript", ["TypeScript", "C++"])
tuple7[3][0] = "newValue1"
tuple7[3][1] = "newValue2"
print(tuple7)  # ('Python', 'Java', 'JavaScript', ['newValue1', 'newValue2'])


""" =============================================================================== """
""" ===========================  Iterating over a tuple  ========================== """
""" =============================================================================== """
# while loop
index = 0
while index < len(tuple6):
    element = tuple6[index]
    print(element)
    index += 1

# For loop
for element in tuple6:
    print(element)