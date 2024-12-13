# main.py
from todooperations import TodoOperations

def display_menu():
    print("\n=== Todo List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("====================")

def main():
    todo = TodoOperations()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            print(todo.add_task(task))

        elif choice == '2':
            print("\nTasks:")
            print(todo.view_tasks())

        elif choice == '3':
            task_number = int(input("Enter task number to mark as complete: "))
            print(todo.complete_task(task_number))

        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            print(todo.delete_task(task_number))

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()