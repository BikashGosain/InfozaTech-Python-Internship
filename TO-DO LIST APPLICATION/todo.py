import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    description = input("Enter task description: ").strip()

    if not description:
        print("Task description cannot be empty.")
        return

    while True:
        priority = input(
            "Priority (High/Medium/Low): "
        ).strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            break

        print("Invalid priority. Please choose High, Medium, or Low.")

    while True:
        due_date = input(
            "Due date (YYYY-MM-DD): "
        ).strip()

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    task = {
        "description": description,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def sort_tasks(tasks):
    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    return sorted(
        tasks,
        key=lambda task: (
            priority_order.get(task.get("priority", "Low"), 3),
            task.get("due_date", "9999-12-31")
        )
    )


def view_tasks(tasks):
    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending_tasks:
        print("\nNo pending tasks.")
        return

    pending_tasks = sort_tasks(pending_tasks)

    print("\n========== PENDING TASKS ==========")

    for number, task in enumerate(pending_tasks, start=1):
        print(f"{number}. {task['description']}")
        print(f"   Priority: {task.get('priority', 'Low')}")
        print(f"   Due date: {task.get('due_date', 'Not set')}")


def complete_task(tasks):
    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending_tasks:
        print("\nNo pending tasks.")
        return

    pending_tasks = sort_tasks(pending_tasks)
    view_tasks(tasks)

    try:
        task_number = int(
            input("\nEnter task number to complete: ")
        )

        if 1 <= task_number <= len(pending_tasks):
            pending_tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)

            print("Task completed successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending_tasks:
        print("\nNo pending tasks.")
        return

    pending_tasks = sort_tasks(pending_tasks)
    view_tasks(tasks)

    try:
        task_number = int(
            input("\nEnter task number to delete: ")
        )

        if 1 <= task_number <= len(pending_tasks):
            task_to_delete = pending_tasks[task_number - 1]
            tasks.remove(task_to_delete)
            save_tasks(tasks)

            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n========================================")
        print("       PYTHON TO-DO LIST APPLICATION")
        print("========================================")
        print("Developed by Bikash Gosain. \n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()