# This is a single-line comment

"""  
This is a multi-line comment.
This is a multi-line comment.
"""

money = 50
print("Original balance:", money, "dollars")
cost = 10
print("Bought a ice cream，cost：", cost, "dollars")
print("Bought a coke, cost：", cost, "dollars")
print("Current balance:", money - 2 * cost, "dollars")

# using type() to get the types of literals
print(type(33))  # Will get: class 'int'>
print(type(33.33))  # Will get: <class 'float'>
print(type("hello"))  # Will get: <class 'str'>

# type() can also get the types of variables
name = "YOYO"
name_type = type(name)
print(name_type)  # Will get: <class 'str'>

# data type conversion
# convert number to string
num_str = str(11)
print(type(num_str), num_str)  # Will get: <class 'str'> 11
float_str = str(11.123)
print(type(float_str), float_str)  # <class 'str'> 11.123

# convert string to number(int/float)
num1 = int("11")
print(type(num1), num1)  # <class 'int'> 11
num2 = float("11")
print(type(num2), num2)  # <class 'float'> 11.0

# convert int to float, or float to int
num3 = int(12.13)
print(type(num3), num3)  # <class 'int'> 12
num4 = float(14)
print(type(num4), num4)  # <class 'float'> 14.0
# ALL the content of the string must be numbers, otherwise will result in errors
# print(int("hello"))   Will get: ValueError: invalid literal for int() with base 10: 'hello'


# Arithmetic Operators
print("1 + 1 =", 1 + 1)    # 1 + 1 = 2
print("2 - 1 =", 2 - 1)    # 2 - 1 = 1
print("3 * 3 =", 3 * 3)     # 3 * 3 = 9
print("4 / 2 =", 4 / 2)      # 4 / 2 = 2.0
print("11 // 2 =", 11 // 2)  # 11 // 2= 5
print("9 % 2=", 9 % 2)      # 9 % 2 = 1
print("2 ** 2 =", 2 ** 2)    # 2 ** 2 = 4

name = "KIWI Company"
setup_year = 2024
stock_price = 19.99
message = "%s, founded in: %d, today's stock price is: %.2f" % (name, setup_year, stock_price)
print(message)   # KIWI Company, founded in: 2024, today's stock price is: 19.99
# Or, use the f"{}" method
print(f"{name}, founded in: {setup_year}, today's stock price is: {stock_price} ")

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是: %5d" % num1)
# 输出为：数字11宽度限制5，结果是: 11
# 整数 num1 的宽度被限制为 5，因此在数字前补了 3 个空格。

print("数字11宽度限制1，结果是: %1d" % num1)
# 输出为：数字11宽度限制1，结果是: 11
# 宽度设置为 1，但由于数字自身占 2 位，因此宽度限制无效。

print("数字11.345宽度限制7，小数精度2，结果是: %7.2f" % num2)
# 输出为：数字11.345宽度限制7，小数精度2，结果是: 11.35
# 浮点数 num2 的总宽度限制为 7，小数精度为 2，结果在小数点后保留 2 位，并前面补 2 个空格以达到总宽度 7。

print("数字11.345不限制，小数精度2，结果是: %.2f" % num2)
# 输出为：数字11.345宽度限制7，小数精度2，结果是: 11.35
# 浮点数 num2 的总宽度限制为 7，小数精度为 2，结果在小数点后保留 2 位，并前面补 2 个空格以达到总宽度 7。