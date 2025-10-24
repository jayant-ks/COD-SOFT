# To-Do List Application
tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully.")

    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting... Have a productive day!")
        break

    else:
        print("Invalid choice! Try again.")
