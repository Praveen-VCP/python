def show_tasks(tasks):
    """Displays the to-do list."""
    if not tasks:
        print("\n✅ No tasks in the list!")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []  # List to store tasks

    while True:
        print("\n=== To-Do List Menu ===")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Remove Task")
        print("4️⃣ Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"✅ '{task}' added to the list!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                removed_task = tasks.pop(task_num)
                print(f"🗑️ Removed: '{removed_task}'")
            except (IndexError, ValueError):
                print("❌ Invalid task number!")

        elif choice == "4":
            print("👋 Exiting... Have a great day!")
            break

        else:
            print("⚠️ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
