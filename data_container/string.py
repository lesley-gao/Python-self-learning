""" =============================================================================== """
""" ==================================  string basics  ============================ """
""" =============================================================================== """
sentence = "Hello World!"
print(sentence[0])  # Result: i
print(sentence[-1])  # Result: a


""" =============================================================================== """
""" ================================= methods of string  ========================== """
""" =============================================================================== """
# index()
my_str = "Mumu loves little baby bum"
value = my_str.index("loves")
print(f"The starting index of 'loves' in the string {my_str} is: {value}")
# Result: The starting index of 'loves' in the string Mumu loves little baby bum is: 5

# replace()
new_my_str = my_str.replace("little", "big")
print(f"After replacing, the string {my_str} becomes: {new_my_str}")
# Result: After replacing, the string Mumu loves little baby bum becomes: Mumu loves big baby bum

# split()
my_str = "Mumu loves little baby bum"
my_str_list = my_str.split(" ")
print(f"After splitting the string {my_str}, the result is: {my_str_list}, type is: {type(my_str_list)}")
# Result: After splitting the string Mumu loves little baby bum, the result is: ['Mumu', 'loves', 'little', 'baby', 'bum'], type is: <class 'list'>

# strip()
my_str = "   Mumu loves little baby bum   "
new_my_str = my_str.strip()  # Without arguments, removes leading and trailing whitespace
print(f"After stripping, the string {my_str} becomes: {new_my_str}")
# Result: After stripping, the string    Mumu loves little baby bum    becomes: Mumu loves little baby bum

my_str = "12Mumu loves little baby bum21"
new_my_str = my_str.strip("12")  # With arguments, removes specified characters from the start and end of the string.
                                 # Both "12" and "21" are removed because "1" and "2" are treated separately.
print(f"After stripping, the string {my_str} becomes: {new_my_str}")
# Result: After stripping, the string 12Mumu loves little baby bum21 becomes: Mumu loves little baby bum

# count()
my_str = "Mumu loves little baby bum and little huahua"
count = my_str.count("little")
print(f"The substring 'little' appears in the string {my_str} {count} times")
# Result: The substring 'little' appears in the string Mumu loves little baby bum and little huahua 2 times

# len()
num = len(my_str)
print(f"The length of the string {my_str} is: {num}")
# Result: The length of the string Mumu loves little baby bum and little huahua is: 44


""" =============================================================================== """
""" ===========================  Iterating over a string  ========================== """
""" =============================================================================== """
new_str = "Learning Python"
# while loop
index = 0
while index < len(new_str):
    element = new_str[index]
    print(element)
    index += 1

# For loop
for element in new_str:
    print(element)


