"""
Write a Python program that does the following:

Takes user input for a list of numbers (comma-separated).
Converts the input into a list of integers.
Pass the list to a function and do the sum and print the output
"""

def sum_of_numbers(numbers):
    return sum(numbers)

# Taking user input
user_input = input("Enter numbers separated by commas: ")

# Converting input string to a list of integers
num_list = [int(num) for num in user_input.split(',')]

# Calling the function and printing the result
result = sum_of_numbers(num_list)
print("Sum of numbers:", result)

