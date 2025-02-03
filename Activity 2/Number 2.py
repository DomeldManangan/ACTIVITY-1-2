# 2. Create a program will show if the given input number is a prime number (a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 e.g. 2, 3, 5, 7, 11). Use looping statement to solve the problem.

number = int(input("Enter a number to check if it is prime: "))

if number > 1:
    is_prime = True  
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False 
            break
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")
