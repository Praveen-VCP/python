# Integer and Float

num1 = int(input("Enter an integer: "))  # Taking integer input
num2 = float(input("Enter a float: "))   # Taking float input

print(f"Integer: {num1}, Float: {num2}")
print(f"Sum: {num1 + num2}, Multiplication: {num1 * num2}")

# String
text = input("Enter a string: ")
print(f"Uppercase: {text.upper()}, Length: {len(text)}")

# List
num_list = [10, 20, 30, 40, 50]
print(f"Original List: {num_list}")
num_list.append(60)  # Adding an element
print(f"Updated List: {num_list}")

# Tuple
num_tuple = (1, 2, 3, 4, 5)
print(f"Tuple: {num_tuple}, Second Element: {num_tuple[1]}")

# Set (Removes Duplicates)
num_set = {1, 2, 3, 3, 4, 5}
print(f"Set (No Duplicates): {num_set}")
num_set.add(6)
print(f"Updated Set: {num_set}")

# Dictionary (Key-Value Pairs)
student = {"name": "praveen", "age": 22, "course": "Python"}
print(f"Student Dictionary: {student}")
print(f"Student Name: {student['name']}")

# Boolean
is_adult = num1 >= 25  # Boolean condition
print(f"Is Adult? {is_adult}")