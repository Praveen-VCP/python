#this is python basic code for beginner
def example():
    print("Wrong indentation!")  # Indented 2 spaces instead of 4
def age():
    print(22)

def find_my_name():
    print("My name is Praveen")  # Updated to display a clearer message


find_my_name()
age()
example()

# This is a single-line comment
print("Hello, World!")
print(2 * 8)  # Added spaces around the multiplication operator for consistency
print("54")
x=100
print(x)
x=x+10
print(x)
x=x*10
print(x)
x=x/10
print(x)
x=x-10
print(x)
x=x**2
print(x)
x=x%2
print(x)
x=x//2
print(x)





x = 10  # Initialize x with the value 10
y = x * 2  # Double the value of x and store it in y


# This is a multi-line comment
# Each line starts with a hash symbol
# Use this method for multi-line explanations


"""
Python (the programming language)
A general-purpose programming language that's used to build websites and software, automate tasks, and analyze data 
Developed by Guido van Rossum and released in 1991 
Named after the British comedy group Monty Python 
Considered easy to learn, making it popular with non-programmers 
Used in many fields, including data analysis, artificial intelligence, and scientific research 
A dynamic, interpreted language that's short and flexible 
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
