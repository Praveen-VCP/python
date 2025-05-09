"""
Asks the user to enter product names and prices (comma-separated).
Stores them in a dictionary.
Asks the user to enter a discount percentage.
Calculates and prints the total price before and after applying the discount.
"""
text = "="
print(text*59)
store_name = ("🎄VCP Store🏬🛒")
print(store_name.center(55,"-"))

text = "="
print(text*59)
products_input=input("Enter product names and prices : ")
text = "="
print(text*59)
products = {}
for item in products_input.split(","):
    name,price = item.rsplit(" ",1)
    products[name] =  float(price)
    products[name] =  float(price)

print("product name and price:",products)

text = "="
print(text * 59)



discount_percentage = float(input("Enter discount percentage : "))
total_price = sum(products.values())
discount_amount = (discount_percentage / 100) * total_price
final_price = total_price - discount_amount
# print(products)


print(f" total price before discount : {total_price:.2f}")
print(f"discount amount : {discount_amount:.2f}")
print(f"total price after discount :{final_price:.2f}")

text = "="
print(text*59)







