x = 5
y = "5"
print(x + int(y))

def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3, []))
print(func(4))


x = [1, 2, 3]
y = x
y.append(4)
print(x)

def func(val, lst=[]):
    lst.append(val)
    return lst

print(func(10))
print(func(20))
print(func(30, []))
print(func(40))


x = [1, 2, 3]
y = x[:]
y.append(4)

print(x)
print(y)


def func(a, b):
    return a if a > b else b

print(func(5, 10))
print(func(15, 7))
print(func(8, 8))



a = [10, 20, 30]
b = a
b = b + [40]

print(a)
print(b)


def change_list(lst):
    lst.append(4)
    lst = [1, 2, 3]
    lst.append(5)

my_list = [10, 20, 30]
change_list(my_list)

print(my_list)