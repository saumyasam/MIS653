# Author: Saumya Padhi
# Week 5 MSBA Exercise
def is_prime(n):    # Defining function
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
          return False
    return True
number=int(input("Enter a number to check whether prime or not:"))
prime_check = is_prime(number) # is_prime function is called with number as a value.
print(f"Is {number} prime? {prime_check}")