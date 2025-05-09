def check_even_odd(number):
    if number % 2 ==0:
        return "even"
    else:
        return "odd"


num = int(input("enter a number: "))
print(f"the number {num} is {check_even_odd(num)}."),





"""
1.Write a function named calculatePower that takes two integers, base and exponent,
and returns the result of raising base to the power of exponent.
"""

def calculate_power(base ,exponent):
    return base ** exponent
print(calculate_power(2,3))



"""
2.Write a program to calculate simple interest for a given principal amount,
rate of interest, and time period using a function.
"""
def simple_interest (p,r,t) :
    si = (p*r*t)/100
    return (si)
principle = int(input("Enter a amount :"))
interest = int(input("Enter a interest amount(%) :"))
time = int(input("Enter a time period :"))

result = simple_interest(principle,interest,time)
amount = (result + principle)
print(f"simple interest {result}")
print(f"over all amount ={amount}")




"""
3.Write a Python function named factorial(n) that takes an integer n as input and returns its factorial.
"""
def factorial(n):
    result = 1
    for i in range (1,n+1):
        result *= i
    return result
number = int(input("Enter a number : "))
print(factorial(number))





"""
4.Write a Python function to multiply all the numbers in a list.
Sample list: [4, 2, -1, 6, 3]
"""
def multiply(*n):
    result=1
    for i in n:
        result *= i
    return result

print(multiply(4, 2, -1, 6, 3))




"""
5.Write a Python function to check whether a number falls within a given range.
"""
def check_whether(n):
    if n in range (1,10):
        print(f"{n} in range")
    else:
        print(f"{n} in out of range")
number = int(input("Enter a number : "))
check_whether(number)









