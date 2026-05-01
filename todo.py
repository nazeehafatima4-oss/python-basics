tasks = []

print("📝 Welcome to To-Do List")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, ".", t)

    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
