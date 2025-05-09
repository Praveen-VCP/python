"""
Write a program to count the number of vowels in a string.
"""

def count_vowels(string):
    return sum(1 for letter in string )

# Example usage
#input_string = input("Enter a string: ")
#print("Number of vowels:", count_vowels(input_string))

"""
How do you replace all occurrences of a substring in a given string?
"""
#text = "Hello world! Welcome to the world of Python."
#new_text = text.replace("world", "universe")

# print(new_text)

"""
3. Write a program to count the occurrences of each character in a string using a dictionary.
"""
from collections import Counter

def count_characters(string):
    return dict(Counter(string))  # Convert Counter object to dictionary

# Example usage
input_string = input("Enter a string: ")
print(count_characters(input_string))

"""
4. How do you check if a key exists in a dictionary?
"""
my_dict = {"a": 1, "b": 2, "c": 3}
if "age" in my_dict:
    print("Key exists!")
else:
    print("Key does not exist.")

"""
5. Write a Python program to remove a key from a dictionary.
"""
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["a"]
print(my_dict)

"""
6. How do you find the sum of all values in a dictionary?
"""
my_dict = {"a": 12, "b": 2, "c": 3}
total = sum(my_dict.values())
print(total)

"""
7. Write a program to sort a dictionary by values in ascending and descending order.
"""
my_dict = {"a": 12, "b": 2, "c": 3}
sorted_dict = sorted(my_dict.items(),key= lambda x:x[1], )
print(sorted_dict)

"""
8. How do you invert a dictionary (swap keys and values)?
"""

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v: k for k, v in original_dict.items()}

print(inverted_dict)

"""
9. Write a Python program to find the common keys between two dictionaries.
"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
common_keys = set(dict1.keys()) & set(dict2.keys())
print(common_keys)


"""
10. How do you create a dictionary from two lists where one list contains keys and the other contains values?
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print("dict zip ", my_dict)


"""
11. Write a Python program to remove duplicate values from a dictionary.
"""
original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
seen_values = set()
unique_dict = {k: v for k, v in original_dict.items() if v not in seen_values and not seen_values.add(v)}

print(unique_dict)

"""
12. How do you get a list of all keys and values separately from a dictionary?
"""
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)

"""
13. Write a program to update a dictionary with key-value pairs from another dictionary.
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}

print(merged_dict)

"""
14. How do you check if two dictionaries are equal (have the same key-value pairs)?
"""
praveen = {'a': 1, 'b': 2, 'c': 3}
praveen1 = {'a': 1, 'b': 2, 'c': 3}
print(praveen == praveen1)

"""
15. Write a Python program to get the value of a key safely using get() with a default value.
"""
my_dict = {'name': praveen, 'age': 22}
age = my_dict.get('age', "unknown")
city = my_dict.get('city', "unknown")
print(age)
print(city)


"""
16. How do you find the difference between two dictionaries (keys present in one but not in the other)?
"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

only_in_dict1 = set(dict1.keys()) - set(dict2.keys())
only_in_dict2 = set(dict2.keys()) - set(dict1.keys())

print("Keys only in dict1:", only_in_dict1)
print("Keys only in dict2:", only_in_dict2)

"""
17. Write a Python program to group values in a dictionary based on a common key prefix.
"""
from collections import defaultdict

def group_by_prefix(data):
    grouped_dict = defaultdict(list)

    for key, value in data.items():
        prefix = key.split('_')[0]
        grouped_dict[prefix].append(value)

    return dict(grouped_dict)

data = {
    'fruit_apple': 10,
    'fruit_banana': 20,
    'veg_carrot': 15,
    'veg_broccoli': 25,
    'fruit_mango': 30
}

grouped = group_by_prefix(data)
print(grouped)

"""
18. How do you filter a dictionary based on a condition (e.g., values greater than a threshold)?
"""
my_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
filtered_dict = {k: v for k, v in my_dict.items() if v > 15}

print(filtered_dict)

"""
19. Write a program to count the frequency of words in a given sentence using a dictionary.
"""
from collections import Counter

def word_frequency(sentence):
    words = sentence.lower().split()
    word_count = Counter(words)
    return dict(word_count)


sentence = "This is a test. This test is simple and this test works."
sentence = sentence.replace('.', '')

freq_dict = word_frequency(sentence)
print(freq_dict)

"""
20. How do you create a nested dictionary and access its elements?
"""
details = {
    "praveen" : {"age" :"22","course" : "python" },
}
print("print my age:", details["praveen"]["age"])
