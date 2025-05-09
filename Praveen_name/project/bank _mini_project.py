# from random import choice

accounts = {}

class BankAccount:
    def __init__(self,account_number,account_holder,phone_number,place,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.phone_number = phone_number
        self.place = place

        self.balance = balance

    def deposit(self,account_number,amount):
        if accounts[account_number]:
            account = accounts[account_number]
            if amount > 0:
                account.balance += amount
                print(f"deposit successfully,new balance:{self.balance:.2f}")

        else:
            print("Invalid account details⁉️")

    def withdraw(self,account_number,amount):
        if accounts[account_number]:
            account = accounts[account_number]
            if 0 < amount <= account.balance:
                account.balance -= account
                print(f"Withdraw successfully new balance : {self.balance:.2f}")
            else:
                print("Invalid withdraw amount⁉️ insufficient fund‼️‼️")

    def check_balance(self,account_number,):
        if accounts[account_number]:
            account = accounts[account_number]
            for attr, value in account. __dict__.items():
                print(f"{attr}:{value}")
        else:
            print("Enter invalid account number‼️‼️")

    def transfer(self, receiver_account_number, amount):
        receiver = accounts.get(receiver_account_number)
        if not  receiver:
            print("Invalid  receiver account number‼️‼️")
            return
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            print(f"₹{amount:.2f} transferred successfully to { receiver.account_holder} ({ receiver.account_number}).")
            print(f"Your new balance: ₹{self.balance:.2f}")
        else:
            print("Transfer failed due to insufficient balance or invalid amount.")



def main():
    print("welcome to mahil bank")
    account_number = input("Enter account number🧾 : ")
    account_holder = input("Enter account holder name📛 : ")
    phone_number = input("Enter a phone number☎️ : ")
    place = input("Enter a place🪧 : ")
    print(f"account added{account_holder},{account_number} successfully👍👍")
    account = BankAccount(account_number,account_holder,phone_number,place)
    accounts[account_number] = account

    while True :
        print("\n1️⃣  Deposit💰\n2️⃣  withdraw💸\n3️⃣  check balance💳\n4️⃣  add new account🧾\n5️⃣  Transfer a amount \n6️⃣  Exit📤 ")
        choice = input("Enter a option : ")


        if choice == '1' :
            account_number = input("Enter a account number🧾 : ")
            account = accounts[account_number]
            amount = float(input("Enter deposit amount💰💰💰 : "))
            account.deposit(account_number,amount)

        elif choice == '2':
            account_number = input("Enter a account number🧾 : ")
            account = accounts[account_number]
            amount = float(input("Enter withdraw amount💳 : "))
            account.withdraw(account_number,amount)

        elif choice == '3' :
            account_number = input("Enter a account number🧐🧐 : ")
            account = accounts[account_number]
            account.check_balance(account_number)

        elif choice == '4' :
            main()



        elif choice == '5':
            sender_number = input("Enter your account number🧾 : ")
            sender = accounts.get(sender_number)

            if sender:

                receiver_number = input("Enter  receiver account number🧾 : ")
                amount = float(input("Enter transfer amount💸💸 : ₹"))
                sender.transfer( receiver_number, amount)

            else:
                print("Invalid sender account number‼️‼️")


        elif choice == '6' :
            print("Thank you for visiting mahil bank 🙏🙏🙏")
            break

        else:
            print("invalid choice❗❗please select a valid choice⁉️")


if __name__ == "__main__" :
    main()























vehicles = {
    "Car": 5 ,
    "Bike": 3,
    "Truck": 2,
    "lorry" : 3,
    "luxury car" : 5

}

