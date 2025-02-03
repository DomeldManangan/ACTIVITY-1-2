# 1. Create a program that will compute the sum of the numbers from 1st term up to the last term input by the user.

first_term_number = int(input("Enter first term number: "))
last_term_number = int(input("Enter last term number: "))

total_sum = 0

for number in range(first_term_number, last_term_number + 1):
    total_sum += number

print(f"The sum of the numbers from {first_term_number} to {last_term_number} is {total_sum}")
