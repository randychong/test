# Assignment 1

# num1 = input("Enter your first number: ")
# op = input("Enter in an operator (ex. +, -, *, /): ")
# num2 = input("Enter your second number: ")

# if op == "+":
#     add = print(int(num1) + int(num2))
# elif op == "-":
#         subtract = print(int(num1) - int(num2))
# elif op == "*":   
#         multiply = print(int(num1) * int(num2))
# elif op == "/":
#         divide = print(int(num1) / int(num2))


# Assignment 2

# num3 = int(input("Enter in a number: "))

# isEven = num3 % 2 == 0
# isOdd = num3 % 2 != 0

# if isEven:
#     print("This number is even.")
# elif isOdd:
#     print("This number is odd.")


# Assignment 3

# num4 = int(input("Enter a number: "))

# if (num4 % 3 == 0 and num4 % 5 == 0):
#     print("FizzBuzz")
# elif num4 % 3 == 0:
#     print("Fizz")
# elif num4 % 5 == 0:
#         print("Buzz")

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)