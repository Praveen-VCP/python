

contacts={}


def add_contact(name,phone,email,place,gender):
    contacts[name] = {"phone": phone,"email": email,"place": place,"gender": gender}
    print(f"contact{name}add successfully")

def view_contact():
    if not contacts:
        print("no contact found."),
    else:
        print("\n contact list:")
        for name,  details in contacts.items():
            print(f"name: {name},phone: {details["phone"]},email: {details["email"]},place: {details["place"]},gender: {details["gender"]} ")
            print()

def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"found contact-name:{name},phone:{details["phone"]},email:{details["email"]},place:{details["place"]},gender{details["gender"]}")
    else:
        print(f"contact{name} not fonded")

def update_contact(name,phone=None,email=None,place=None,gender=None):
    if name in contacts:
        if phone :
            contacts[name]["phone"] = phone
        if email in contacts:
            contacts[name]["email"] = email
        if place in contacts :
            contacts[name]["place"] = place
        if gender in contacts:
            contacts[name]["gender"]=gender

        print(f"update {name} contact successfully")
    else:
        print("No contact founded")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"contact {name} deleted successfully")
    else:
        print(f"contact {name} not founded")



def main():
    while True:
        print("\n contact book list ")
        print("1️⃣.  Add contacts")
        print("2️⃣.  view contacts")
        print("3️⃣.  search contacts")
        print("4️⃣.  Update contacts")
        print("5️⃣.  Delete contacts")
        print("6️⃣.  Exit contacts")

        choice = input("Enter your choice : ")

        if choice == "1":
             name  = input("Enter your name📛 : ")
             phone = input("Enter your phone number📞 : ")
             email = input("Enter your email address📧 :  ")
             place = input("Enter your home address🏡 :  ")
             gender= input("Enter your gender \"male or female\"👦⁘⁘👧 :  ")

             add_contact(name,place,email,place,gender)



        elif choice == "2":
            view_contact()


        elif choice == "3":
            name =input("Enter your name : ")
            search_contact(name)

        elif choice == "4":
            name   = input("Enter your name : ")
            phone  = input("Enter your phone number :  ")
            email  = input("Enter your email address : ")
            place  = input("Enter your home address")
            gender = input("Enter your gender \"male or female\" ")
            update_contact(name,phone if phone else None,email if email else None,place if place else None,
                           gender if gender else None)



        elif choice == "5":
            name = input("Enter your name : ")
            delete_contact(name)


        elif choice == "6":
            print("Thank you for visiting")
            break


        else:
            print("invalid choice try again!!!!")




if __name__=="__main__":
    main()








