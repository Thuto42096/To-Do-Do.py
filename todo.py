import json
import os

File_path = "todos.json"

def load_data(file_path):
    """reads data from json file"""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []

def save_data(file_path, data):
    """writes data to json file"""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def create_task(data):
    """creates a new task"""

    task = input("Enter task: ")
    prompt_if_add = input("Do you want to add a due date? (y/n): ")
    if prompt_if_add == "y":
        due_date = input("Enter due date (DD-MM-YYYY): ")

    else:
        due_date = None
        print("Task created successfully!")
    data.append({"task": task, "due_date": due_date})
    save_data(File_path, data)

def list_tasks(data):
    """lists all tasks"""
    for i, task in enumerate(data):
        print(f"{i}. {task['task']} - {task['due_date']}")

def delete_task(data):
    """deletes a task"""
    for i, task in enumerate(data):
        print(f"{i}. {task['task']} - {task['due_date']}")
    task = int(input("Enter task number: "))
    del data[task]
    save_data(File_path, data)
    print("Task deleted successfully!")

def main():
    """main function"""
    data = load_data(File_path)
    while True:
        print("1. Create task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_task(data)
        elif choice == "2":
            list_tasks(data)
        elif choice == "3":
            delete_task(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()