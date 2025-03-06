from datetime import datetime


def generate_bill(customer_name, items):
    bill = []
    bill.append("=" * 40)
    bill.append("         STORE BILL RECEIPT")
    bill.append("=" * 40)
    bill.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    bill.append(f"Customer: {customer_name}")
    bill.append("=" * 40)
    bill.append("Item           Qty    Price    Total")
    bill.append("-" * 40)

    total_amount = 0
    tax_rate = 0.1  # 10% tax

    for item, details in items.items():
        qty = details['quantity']
        price = details['price']
        total = qty * price
        total_amount += total
        bill.append(f"{item:<15} {qty:<5} {price:<7} {total:<7}")

    tax = total_amount * tax_rate
    grand_total = total_amount + tax

    bill.append("-" * 40)
    bill.append(f"Subtotal: {total_amount:.2f}")
    bill.append(f"Tax (10%): {tax:.2f}")
    bill.append(f"Grand Total: {grand_total:.2f}")
    bill.append("=" * 40)
    bill.append("Thank you for shopping with us!")
    bill.append("=" * 40)

    return "\n".join(bill)


def save_bill_to_file(customer_name, bill_text):
    filename = f"bill_{customer_name.replace(' ', '_')}.txt"
    with open(filename, "w") as file:
        file.write(bill_text)
    print(f"Bill saved as {filename}")


if __name__ == "__main__":
    customer_name = input("Enter customer name: ")
    items = {
        "Apple": {"quantity": 2, "price": 100.5},
        "Milk": {"quantity": 1, "price": 50.0},
        "Bread": {"quantity": 3, "price": 35.0},
    }

    bill_text = generate_bill(customer_name, items)
    print(bill_text)
    save_bill_to_file(customer_name, bill_text)
