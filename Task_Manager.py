import json
import os

TASK_FILE = "tasks.json"

#load existing tasks
def load_task():
   if not os.path.exists(TASK_FILE):
     return []
   with open(TASK_FILE,"r") as file:
     return json.load(file)

#Save tasks:
def save_tasks(tasks):
  with open(TASK_FILE, "w") as file:
     json.dump(tasks, file, indent=4)

#Add task:
def add_task():
  task = input("Enter task:")
  tasks = load_task()
  tasks.append({"task": task, "done": False})
  save_tasks(tasks)
  print("Task added! \n")

#view tasks

def view_tasks():
   tasks = load_task()
   if not tasks:
     print("NO tasks yet.\n")
     return
   print("\n your Tasks:")
   for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. {t['task']} [{status}]")
   print()

def mark_task():
    tasks = load_task()
    view_tasks()

    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete!\n")
    except:
        print("Invalid input\n")

def delete_task():
    tasks = load_task()
    view_tasks()

    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted!\n")
    except:
        print("Invalid input\n")


# Main loop
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3.Mark Task Complete")
    print("4.Delete Task")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option\n")
