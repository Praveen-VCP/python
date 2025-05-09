#lamda

def add(x, y):
    return x + y



add_lambda = lambda x, y: x + y

print(add(3, 4))
print(add_lambda(3, 4))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)



numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)



students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1],reverse=True)
print(sorted_students)

def multiplier(n):
    return lambda x: x * n




double = multiplier(2)
print(double(5))



numbers = [2, 4, 6, 8, 10]


has_odd = any(map(lambda x: x % 2 != 0, numbers))
print(has_odd)

all_even = all(map(lambda x: x % 2 == 0, numbers))
print(all_even)


students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

oldest_student = max(students, key=lambda x: x[1])
print(oldest_student)

youngest_student = min(students, key=lambda x: x[1])
print(youngest_student)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

summed = list(map(lambda x: x[0] + x[1], zip(list1, list2)))
print(summed)


#
complex_func = lambda x: (x ** 2 + 3) / (x - 1) if x != 1 else "Error"
print(complex_func)



def complex_functions(x):
    if x == 1:
        return "Error"
    return (x ** 2 + 3) / (x - 1)
print({complex_functions})

string3 = """ def This is a multi-line 
string in Python."""
print(string3)


text = "    Python      "
print(text.strip())  # Output: "Python" (Removes both sides)
print(text.lstrip()) # Output: "Python  " (Removes left spaces)
print(text.rstrip()) # Output: "  Python" (Removes right spaces)






