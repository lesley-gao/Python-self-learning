""" For Loop Examples """

"""
Example 1: 
Count the Number of "a"s in a sentence
"""
sentence = "We're all travelling through time together, everyday of our lives. All we can do is do our best to relish this remarkable ride."
count_of_a = 0
for letter in sentence.lower():
    if letter == "a":
        count_of_a += 1
print(f"There are altogether {count_of_a} \"a\" in the sentence \"{sentence}\“ ")


"""
Example 2: 
Count the number of even numbers in a range 
"""
num = 100
count = 0
for x in range(1, num + 1):
    if x % 2 == 0:
        count += 1
print(f"There are altogether {count} even numbers in the range from 1 to {num}.")


"""
Example 3: Use a nested for loop
100 days of confession, 10 roses for each day.
That is, each day has a "confession" along with 10 roses, for a total of 100 days.
"""
i = 1
for i in range(1, 101):
    print(f"Day {i}, I love you babe")

    j = 1
    for j in range (1, 11):
        print(f"{j} rose(s) for you")
        j += 1

    i += 1


"""
Example 4: Use a nested for loop
Create a multiplication table up to 9*9 
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end='')
    print()
