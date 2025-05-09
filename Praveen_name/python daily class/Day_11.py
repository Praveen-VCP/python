from itertools import count

text = "="
print(text.center(70, "="))

"""
How i can slice tuple in middle
"""


t = (1,2,3,4,5,6)

center = len(t)//2

left_half = t[2:5]
center_valu = (t[center:])
right_half = t[center:]

print(left_half)
print(center_valu)
print(right_half)


text = "="
print(text.center(70, "="))

"""
Tuple give four element 
Name,Age,Profession,G-mail
"""

person = ("Praveen","22","full stack developer","praveen@gmail.com")
name,age,profession,email = person
print(person)
print(name)
# print person_info for id verfication
person_info = name,age,profession,email
print(person_info)

print(id(person))
print(id(person_info))

text = "="
print(text*70)


combain = ("praveen",22,7.25,True,False,{"name":"praveen","age":22},
           [1,3,2,5,585,])
mid = len(combain)//2
first_half = combain[:mid]
second_half = combain[mid:]
print(first_half)
print(second_half)

counter =1

text = "🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚🔚"
print(text.center(30, "🔚"))
