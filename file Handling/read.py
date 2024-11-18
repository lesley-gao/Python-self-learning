import time


# Open file - open()
f = open("D:/test.txt", "r", encoding="UTF-8")
print(type(f))       # <class '_io.TextIOWrapper'>

# Read file - read()
print(f.read(10))   # read(10) means read the first 10 characters (or bytes if the file is binary).
print(f.read())   # The second read() continues reading from where the previous read() left off,
                 # which in this case means reading all the remaining data in the file starting from the 11th character.


print("----------------------------------------------------------------")
"""In Python, when there are multiple read operations (such as read(), readline(), or readlines()), 
subsequent reads will start from where the previous read operation stopped, i.e., the current position of the file pointer.
If we want to re-read the file from the beginning, we can use f.seek(0) to reset the file pointer to the start of the file.
"""
f.seek(0)

# Read file - readlines()
lines = f.readlines()  # Reads all lines of the file and stores them as a list
print(f"The type of lines is: {type(lines)}")    # The type of lines is: <class 'list'>
print(lines)


print("----------------------------------------------------------------")
f.seek(0)
# Read file - readline(), read one line at a time
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f'First line: {line1}')
print(f'Second Line: {line2}')
print(f'Second Line: {line3}')


print("----------------------------------------------------------------")
# Read file using for loop
f.seek(0)
for line in f:
    print(line)


print("----------------------------------------------------------------")
# Close file  - close()
# Option 1:
# f.close()
# time.sleep(500000)

# Option 2:
# Using "with open()" to operate on a file
# with open("D:/test.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"The data in each line is: {line}")
#
# time.sleep(500000)


print("-------------------------------Practice---------------------------------")
# TODO : It reads each line of the file , counts the occurrences of "it"
# Option 1:
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    content = f.read()
    count = content.count("it")
print(f"The word 'IT' appears for {count} times")

# Option 2:
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    it_times = 0
    for line in f:
        count = line.count("it")
        it_times += count
print(f"The word 'IT' appears for {it_times} times")

