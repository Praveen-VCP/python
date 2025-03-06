def get_valid_age():
    """Prompts user for age and ensures it is a valid integer."""
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            return int(age_input)
        else:
            print("Invalid input. Please enter a valid integer for age.")

def convert_height(height_input):
    """Converts height to meters if given in centimeters."""
    try:
        if height_input.lower().endswith("cm"):
            return float(height_input[:-2]) / 100
        elif height_input.lower().endswith("m"):
            return float(height_input[:-1])
        else:
            return float(height_input)
    except ValueError:
        print("Invalid height format. Please enter a number followed by 'cm' or 'm'.")
        return None

# Taking user input
name = input("Enter your name: ")
age = get_valid_age()

# Ensure valid height input
while True:
    height_input = input("Enter your height (e.g., 180cm or 1.8m): ")
    height = convert_height(height_input)
    if height is not None:
        break

# Storing data in a dictionary
person_info = {
    "name": name,
    "age": age,
    "height_m": height
}

# Display stored data
print("\nStored Information:")
print(person_info)


