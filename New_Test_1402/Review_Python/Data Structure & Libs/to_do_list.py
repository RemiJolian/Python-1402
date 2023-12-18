import tkinter as tk

def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_entry.delete(0)
    task_list.bind('<Configure>', update_tasks)

def delete_task(event):
    index = task_listbox.curselection()
    if index:
        task_list.pop(index)

def update_tasks():
    task_listbox.bind('<Configure>', update_tasks)
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.add(task)

def main():
    root = tk.Tk()
    root.title("To-Do List")

    task_list = []
    task_listbox = tk.Listbox(root)
    task_listbox.bind('<Configure>', update_tasks)
    task_listbox.pack()

    task_entry = tk.Entry(root)
    task_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
