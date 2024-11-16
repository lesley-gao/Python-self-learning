# A very simple function to get the length of a string
def str_length(data):
    length = 0
    for i in data:
        length +=1
    print(f"The length of the string is {length}")

str_length("hello world")
str_length("Do you love Python?")


# A function that returns a value
def add(a, b):
    return a+b

result = add(10, 20)
print(result)


"""If a function doesn't explicitly return a value (i.e., it lacks a return statement), it will implicitly return None.
None can be used in conditional statements to check if a variable has a meaningful value.
For example：
if value is None:
    print("The value is empty or uninitialized.")
"""
def sayhi():
    print("Hello!")
result = sayhi();
print(f"The return value of sayhi() is {result}") # The return value of sayhi() is None
print(f"The data type of the return value is {type(result)}") # The data type of the return value is <class 'NoneType'>


# Using "global" keyword to modify the global variable inside a function
num = 100
def print_num():
    print(num)
def print_again():
    global num   # Declares that we are using the global variable num
    num = 500
    print(num)
print_num()
print_again()
print(num)


# Practice: Using ATM
def main_menu(username):
    while True:
        print("--------------------Main Menu--------------------")
        print(f"Hello {username}, welcome to Yoyo Bank ATM. Please select an operation:")
        option = input("Check Balance: Enter 1\nDeposit: Enter 2\nWithdraw: Enter 3\nExit: Enter 4\n")
        if option == "1":
            check_balance(username)
        elif option == "2":
            deposit(username)
        elif option == "3":
            withdraw(username)
        elif option == "4":
            print(f"Thank you for using Yoyo Bank ATM, {username}. Bye!")
            break
        else:
            print("Invalid input, please make a new selection!")

def withdraw(username):
    global money
    try:
        withdraw_amount = int(input("Please enter your withdraw amount: "))
        if withdraw_amount > money:
            print("Insufficient balance! Withdraw failed.")
        else:
            money -= withdraw_amount
            print("--------------------Withdraw--------------------")
            print(f"Hello {username}, your withdraw of ${withdraw_amount} is successful")
            print(f"Hello {username}, your remaining balance is: ${money}")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def deposit(username):
    global money
    try:
        deposit_amount = int(input("Please enter your deposit amount: "))
        if deposit_amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            money += deposit_amount
            print("--------------------Deposit--------------------")
            print(f"Hello {username}, your deposit of ${deposit_amount} is successful")
            print(f"Hello {username}, your remaining balance is: ${money}")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def check_balance(username):
    global money
    print("--------------------Check Balance--------------------")
    print(f"Hello {username}, your remaining balance is: ${money}")

money = 5000000
name = input("Please enter your name: ")
main_menu(name)

