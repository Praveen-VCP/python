import os
from datetime import datetime

vehicles = {
    "car": 5,
    "bike": 3,
    "truck": 2,
    "lorry": 8,
    "luxury car": 4


}

vehicles_file = "vehicles.txt"
rented_file = "rented.txt"
history_file = "history.txt"


def normalize_name(name):
    return name.strip().lower()


def load_vehicles():
    try:
        with open(vehicles_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    name, count = line.strip().split(":")
                    vehicles[normalize_name(name)] = int(count)
    except FileNotFoundError:
        save_vehicles()


def save_vehicles():
    with open(vehicles_file, "w") as file:
        for vehicle, count in vehicles.items():
            file.write(f"{vehicle}:{count}\n")


def view_vehicles():
    print("\nAvailable Vehicles:")
    for vehicle, count in vehicles.items():
        print(f"{vehicle.title()}: {count} available")


def rent_vehicle(vehicle):
    vehicle = normalize_name(vehicle)
    if vehicle not in vehicles:
        print("Invalid vehicle name. Please choose from:", ", ".join(vehicles.keys()))
        return

    if vehicles[vehicle] <= 0:
        print("Sorry, this vehicle is currently not available!")
        return

    vehicles[vehicle] -= 1
    save_vehicles()

    with open(rented_file, "a") as file:
        file.write(f"{vehicle}\n")

    with open(history_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Rented: {vehicle}\n")

    print(f"{vehicle.title()} has been rented successfully!")


def return_vehicle(vehicle):
    vehicle = normalize_name(vehicle)
    try:
        with open(rented_file, "r") as file:
            rented_vehicles = [v.strip() for v in file.readlines() if v.strip()]

        if vehicle not in rented_vehicles:
            print("This vehicle was not rented.")
            return

        rented_vehicles.remove(vehicle)
        vehicles[vehicle] += 1
        save_vehicles()

        with open(rented_file, "w") as file:
            if rented_vehicles:
                file.write("\n".join(rented_vehicles) + "\n")
            else:
                file.write("")

        with open(history_file, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Returned: {vehicle}\n")

        print(f"{vehicle.title()} has been returned successfully!")
    except FileNotFoundError:
        print("No rented vehicles found.")


def rental_history():
    try:
        with open(history_file, "r") as file:
            history = file.readlines()
            if not history:
                print("No rental history found.")
                return

        print("\nRental History:")
        for record in history:
            print(record.strip())
    except FileNotFoundError:
        print("No rental history found.")


def clear_rental_history():
    confirm = input("Are you sure you want to clear the rental history? (yes/no): ").strip().lower()
    if confirm == "yes":
        open(history_file, "w").close()
        print("Rental history cleared successfully.")
    else:
        print("Action cancelled.")


def main():
    load_vehicles()
    while True:
        print("\n--- Vehicle Rental System ---")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Rental History")
        print("5. Delete a Vehicle")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_vehicles()
        elif choice == "2":
            vehicle = input("Enter vehicle name to rent: ")
            rent_vehicle(vehicle)
        elif choice == "3":
            vehicle = input("Enter vehicle name to return: ")
            return_vehicle(vehicle)
        elif choice == "4":
            rental_history()
        elif choice == "5":
            clear_rental_history()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("\033[31mInvalid choice, please try again.\033[0m")


if __name__ == "__main__":
    main()
