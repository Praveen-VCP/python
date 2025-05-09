print("output")

# Checking Variable Types
x = 25
print(type(x))


# x = 12
#  print(x)
#  del x
#  print(x)

# Casting variables
s = "10"
n = int(s)
cnt = 5
f = float(cnt)
age = 25
s2 = str(age)

print(type(n))
print(type(f))
print(type(s2))

# Object Reference
x = [100, 200, 300]
y = x
print(y)

# list type
x = [8, 6, 9]
y = x

print(id(x))
print(id(y))

# Immutable
c = 60
d = c
c = 80
print(c)
print(d)

# (Equality Operator) vs (Identity Operator)
x = [1, 5, 2]
y = [1, 2, 3]

print(x == y)
print(x is y)

x = [10, 20, 30]
y = [10, 20, 30]

print(x == y)
print(x is y)

# Garbage Collection

x = [1, 2, 3]
x =None
print(x)
