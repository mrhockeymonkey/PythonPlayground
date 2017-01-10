"""
The Collatz sequence is define as taking any integer and dividing it by 2 if even,
or multiplying it by 3 and adding 1 if odd. This sequence will always give 1 no matter
the integer used.
"""

# Define the function collatz which returns 
def collatz(number) :
	if (number % 2 == 0) :
		return number // 2
	else :
		return 3 * number + 1

# Prompt for user input and convert str to int
user_input = input("Enter Integer: ")
number = int(user_input)

# Create a sequence of numbers using collatz until we hit 1
while number != 1 :
	number = collatz(number)
	print(number)
