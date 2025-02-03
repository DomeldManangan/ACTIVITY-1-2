# Program to find the highest of three numbers
# 1. Create a program that will ask the user to enter three numbers and display which number is highest.
# Taking user input

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"The highest number is {num1}")
    else:
        print(f"The highest number is {num3}")
elif num2 >= num3:
    print(f"The highest number is {num2}")
else:
    print(f"The highest number is {num3}")