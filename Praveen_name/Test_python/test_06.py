# from Test_python.Test_05 import details
# from tkinter.font import names

contacts = {}

def add_contact(name,phone,email):
    contacts[name]= {"phone":phone, "email":email}
    print(f"contact {name}add successfully.")

def view_contact():
    if not contacts:
        print("no contact found."),
    else:
        print("\n contact list:")
        for name,  details in contacts.items():
            print(f"name:{name},phone:{details["phone"]},email:{details["email"]}")
            print()

def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"Found Contact - Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print(f"found contact{name}not found")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email :
            contacts[name]["email"] = email
        print(f"contact{name}successfully.")
    else:
        print(f"contact{name}not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
    print(f"contact {name} deleted successfully🗑️🗑️🗑️.")


def main ():
    while True:
        print("\n 🦋contact book menu:")
        print("1️⃣  Add contact")
        print("2️⃣  view contact")
        print("3️⃣  search contact")
        print("4️⃣  update contact")
        print("5️⃣  delete contact")
        print("6️⃣  exit contact")

        choice = input("Enter your choice🤔 : ")

        if choice == '1':
            name = input("Enter a name📛 : ")
            phone = input("Enter a number☎️ : ")
            email = input("Enter a email I'd🆔  : ")
            add_contact(name,phone,email)
        elif choice =='2':
            view_contact()
        elif choice == '3':
            name = input("Enter a name📛 : ")
            search_contact(name)
        elif choice =='4':
            name = input("Enter a new name📛 : ")
            phone = input("Enter a new number(skip the opp)☎️ : ")
            email = input("Enter a email(skip the email)🆔 : ")
            update_contact(name,phone if phone else None,email if email else None)
        elif choice =='5':
            name = input("Enter a name to delete 🗑️🗑️: ")
            delete_contact(name)
        elif choice == '6':
            print("Thank you for visiting.have a nice day🙏🙏🙏")
            break
        else:
            print("Invaild choice number. try again ")



if __name__ =="__main__":
    main()





