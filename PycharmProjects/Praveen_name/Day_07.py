#QESTION_01


x = 10

def print_x():
    print(x)

print_x()

# QUESTION_02
def my_function():
    y = 20
    print(y)


my_function()

# print(y)

# QUESTION_03

def my_function():
    z = 30
    print(z)
my_function()


# print(z)
# QUESTION(04)
x = 10
print(id(x))
def modify_x():
    x = 15
    print(x)
    print(x is x)
    print(id(x))

modify_x()
print(x)

x = 10
# QUESTION(05)
def modify_x():
    global x
    x = x + 5
    print("Inside function:", x)


modify_x()


print("Outside function:", x)

