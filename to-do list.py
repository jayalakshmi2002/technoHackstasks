# Create an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list!")

# Function to display the to-do list
def display_list():
    print("To-Do List:")
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        for task in todo_list:
            print("- " + task)

# Main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")