name = input("Please enter your name : ")
numbers = []
for num in range(3):
    num = int(input(f"Enter your favorite number {num+1}: "))
    numbers.append(num)

print(f"Welcome, {name}! Enter your favourite numbers.")

even_odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

print("Here's more info about your numbers :")
for num, parity in even_odd_list:
    print(f"  {num} is {parity}!")

sum_of_numbers = sum (numbers)
print(f"The sum of your numbers is: {sum_of_numbers}")

print("Let's see if it's a prime number...")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(sum_of_numbers):
    print("And... it's a prime number! Congratulations!")
else:
    print("Not a prime number, but still a great number!")