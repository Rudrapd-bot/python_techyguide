# To-Do List Manager

tasks = []

# Function to add task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!\n")

# Function to remove task
def remove_task():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        display_tasks()
        task_num = int(input("Enter task number to remove: "))
        
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed successfully!\n")
        else:
            print("Invalid task number!\n")

# Function to display tasks
def display_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.\n")
    else:
        print("\nTo-Do List:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print()

# Function to count tasks
def count_tasks():
    print(f"Total tasks: {len(tasks)}\n")

# Main program
while True:
    print("===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Count Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()

    elif choice == '2':
        remove_task()

    elif choice == '3':
        display_tasks()

    elif choice == '4':
        count_tasks()

    elif choice == '5':
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.\n")