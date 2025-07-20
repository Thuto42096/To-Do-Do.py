# to-do-do/todo/__main__.py


import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_PATH = "todos.json"

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TODODO - To Do List App")

        self.data = load_data(FILE_PATH)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=30, background="lightblue")
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task, width=30, background="lightcoral")
        self.delete_button.pack()

        self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.data):
            due = f" (Due: {task['due_date']})" if task["due_date"] else ""
            self.task_listbox.insert(tk.END, f"{i + 1}. {task['task']}{due}")

    def add_task(self):
        task_name = self.task_entry.get().strip()
        if not task_name:
            messagebox.showwarning("Input Error", "Task name cannot be empty.")
            return

        due_date = None
        if messagebox.askyesno("Due Date", "Add a due date?"):
            due_date = simpledialog.askstring("Due Date", "Enter due date (DD-MM-YYYY):")

        self.data.append({"task": task_name, "due_date": due_date})
        save_data(FILE_PATH, self.data)
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        index = selected[0]
        del self.data[index]
        save_data(FILE_PATH, self.data)
        self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()