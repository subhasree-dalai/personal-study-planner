import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    print("\n--- Add New Task ---")
    task_name = input("Enter task name: ").strip()
    subject = input("Enter subject name: ").strip()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    if not task_name or not subject or not deadline:
        print("Task name, subject, and deadline cannot be empty.")
        return

    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Setting priority to Medium.")
        priority = "Medium"

    task = {
        "task_name": task_name,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    print("\n--- All Tasks ---")
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"\nTask {i}")
        print(f"Task Name : {task['task_name']}")
        print(f"Subject   : {task['subject']}")
        print(f"Deadline  : {task['deadline']}")
        print(f"Priority  : {task['priority']}")
        print(f"Status    : {task['status']}")


def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task_name']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def search_by_subject(tasks):
    print("\n--- Search Tasks by Subject ---")
    subject_name = input("Enter subject name to search: ").strip().lower()

    found = False
    for i, task in enumerate(tasks, start=1):
        if task["subject"].lower() == subject_name:
            found = True
            print(f"\nTask {i}")
            print(f"Task Name : {task['task_name']}")
            print(f"Subject   : {task['subject']}")
            print(f"Deadline  : {task['deadline']}")
            print(f"Priority  : {task['priority']}")
            print(f"Status    : {task['status']}")

    if not found:
        print("No tasks found for this subject.")


def show_overdue_tasks(tasks):
    print("\n--- Overdue Tasks ---")
    today = datetime.today().date()
    found = False

    for i, task in enumerate(tasks, start=1):
        deadline_date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        if task["status"] == "Pending" and deadline_date < today:
            found = True
            print(f"\nTask {i}")
            print(f"Task Name : {task['task_name']}")
            print(f"Subject   : {task['subject']}")
            print(f"Deadline  : {task['deadline']}")
            print(f"Priority  : {task['priority']}")
            print(f"Status    : {task['status']}")

    if not found:
        print("No overdue tasks found.")


def main():
    tasks = load_tasks()

    while True:
        print("\n========== Personal Study Planner ==========")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Search Tasks by Subject")
        print("6. Show Overdue Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_by_subject(tasks)
        elif choice == "6":
            show_overdue_tasks(tasks)
        elif choice == "7":
            print("Thank you for using Personal Study Planner.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()