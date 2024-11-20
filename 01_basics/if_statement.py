
# OPTION 1
print("Welcome to Kid Space entertainment park. ")
height = input("Please enter your height(cm): ")
vip_level = input("Please enter your VIP level(1-5): ")
if int(height) < 120:
    print("You do not exceed the restricted height of 120cm, please enjoy your free entry here.")
elif int(vip_level) > 3:
    print("Your VIP level is higher than 3, please enjoy your free entry here.")
else:
    print("Sorry, you have to buy a ticket for $10.")
print("Hope you have a wonderful day!")

# OPTION 2: more concise
print("Welcome to Kid Space entertainment park. ")
if int(input("Please enter your height(cm): ")) < 120:
    print("You do not exceed the restricted height of 120cm, please enjoy your free entry here.")
elif int(input("Please enter your VIP level(1-5): ")) > 3:
    print("Your VIP level is higher than 3, please enjoy your free entry here.")
else:
    print("Sorry, you have to buy a ticket for $10.")
print("Hope you have a wonderful day!")


# Example: guess numbers
num = 10
if int(input("Please enter your first guess: ")) == num:
    print("You are right!")
elif int(input("Nah, guess again: ")) == num:
    print("You are right!")
elif int(input("Nah, last guess: ")) == num:
    print("BINGO!")
else:
    print(f"Sorry, your guesses are all wrong. The number in my heart is {num}")


"""
NO LOOPS ALLOWED:
A random number between 1 and 10 will be generated. 
You have 3 attempts to guess it. 
After each incorrect guess, you'll be told if your number is too high or too low.
"""
import random
right_number = random.randint(1, 10)

guess_number = int(input("Please enter your first guess:"))
if guess_number == right_number:
    print("YEAH! You guess it right!")
else:
    if guess_number > right_number:
        print("Your guess is too large!")
    else:
        print("Your guess is too small!")

    guess_number = int(input("Second chance! Please guess again: "))
    if guess_number == right_number:
        print("YEAH! You guess it right!")
    else:
        if guess_number > right_number:
            print("Your guess is too large!")
        else:
            print("Your guess is too small!")

        guess_number = int(input("Third chance! Please guess again: "))
        if guess_number == right_number:
            print("YEAH! You guess it right!")
        else:
            print("Oops! You have no more guesses.")