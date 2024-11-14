""" While Loop Examples """

"""
Example 1: 
Say "I love you" for 100 times"""
# i = 0
# while i < 100:
#     print(f"I love you")
#     i += 1


"""
Example 2: 
Calculate the sum of all numbers from 1 to 100"""
# i = 1
# sum_number = 0
# while i <= 100:
#     sum_number += i
#     i += 1
# print(sum_number)


"""
Example 3: 
Set a random integer variable within the range of 1-100.
Use a while loop, along with the input statement, to check if the entered number is equal to the random number.
- Provide unlimited attempts until the correct number is guessed.
- Each time the guess is incorrect, indicate if the guess is too high or too low.
- After guessing the number, display how many attempts were made.
"""
import random
guess_count = 1
target_number = random.randint(1,100)
guess_number = int(input("Please enter your guess"))
while guess_number != target_number:
    if guess_number > target_number:
        print("Your guess is too large.")
    else:
        print("Your guess is too small")
    guess_number = int(input("Please enter your guess"))
    guess_count += 1
print(f"You got the right numbers after {guess_count} guesses.")


"""
Example 4: Use a nested while loop
100 days of confession, 10 roses for each day.
That is, each day has a "confession" along with 10 roses, for a total of 100 days.
"""
day = 1
while day <= 100:
    print(f"I love you babe. It's day {day}.")
    rose_quantity = 1
    while rose_quantity <= 10:
        print(f"{rose_quantity} rose(s) for you!")
        rose_quantity += 1
    day += 1


"""
Example 5: Use a nested while loop
Create a multiplication table up to 9*9 
"""
i = 1
while i <=9:

    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1

    i += 1
    print() #adds a newline after each row so that the next row starts on a new line.

