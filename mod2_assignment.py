# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = int(num1_str)
num2 = int(num2_str)

sum = num1 + num2
print("Addition:", sum)

substraction = num1 - num2
print("Substraction:", substraction)

multiplication = num1 * num2
print("Multiplication:", multiplication)

division = num1 / num2
print("Division:", division)


# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

first_name = first_name.capitalize()
last_name = last_name.capitalize()

print("Hello," + first_name + " " + last_name + "!" + " Welcome to Python program.")