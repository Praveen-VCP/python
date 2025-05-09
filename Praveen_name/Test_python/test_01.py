print("output")


"""
Q1. Assign a value to a variable x = 100 and
 create another variable y that references x.
Change the value of x and check if y is affected.
"""


x = 100
y = x

print("x Before changing")
print(f"x = {x},y={y}")

x = 2003
print("x After changing")
print(f"x = {x},y={y}")

"""
Q2.Create a list list1 = [1, 2, 3] and assign list2 = list1. 
Modify list1 by appending a new element.
 What happens to list2?
 """

list1 = [1, 2, 3]
list2 = list1
print("list1 Before appending")
print(f"list1 = {list1},list2={list2}")

list1.append(4)
print("list1 After appending")
print(f"list1 = {list1},list2={list2}")

"""
Q3. Use the id() function to compare memory addresses of 
two variables pointing to the same integer.
"""
x = 100
y = x
width = 25
print(f" x = {id(x)}")
print(f" y = {id(y)}")

# print("True or False")
print(" If X and Y is same ID print")
answer = "True or False : "f"{x is y}"

print(f"{answer:^28}")

"""
Q4. Check if two string variables with 
the same value refer to the same object in memory using the is operator.
"""

str1 = "Hello"
str2 = "Hello"
print(f"str1 = {id(str1)}")
print(f"str2 = {id(str2)}")

print("print true or false")
print(f"{str1 is str2}")

"""
Q5. Create a dictionary storing details of a student
 (name, age, grade). Print the value of "grade".
"""

student = {"name": "Praveen", "age": 22, "grade": "A"}
print("Student Name: {} , Age: {}, Grade: {}"
      .format(student["name"],
              student["age"],
              student["grade"]))

"""
Q6. Create a dictionary, assign it to another variable,
 modify one key-value pair, and check if both variables are affected.
"""

student = {"name": "Praveen", "age": 22, "grade": "A"}

student_copy = student

print(f"student = {student}")
print(f"student_copy = {student_copy}")

student["grade"] = "B"
print(f"student = {student}")
print(f"student_copy = {student_copy}")


"""
Q7. Define a function that takes an immutable data type 
(like an integer or string) as an argument and modifies it inside the function. 
Check if the original variable is affected.
"""

def modify_integer(num):
    print(f"Inside function (before modification): {num}, Memory Address: {id(num)}")
    num = num + 10
    print(f"Inside function (after modification): {num}, Memory Address: {id(num)}")


x = int(input("enter a number:"))
print(f"Before function call: {x}, Memory Address: {id(x)}")
modify_integer(x)
print(f"After function call: {x}, Memory Address: {id(x)}")












