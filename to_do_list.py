from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task_data = line.strip().split("|")
                    task = {
                        "task": task_data[0],
                        "priority": task_data[1],
                        "due_date": task_data[2],
                        "completed": task_data[3] == "True",
                    }
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # File does not exist yet

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['priority']}|{task['due_date']}|{task['completed']}\n")

    def show_menu(self):
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

    def add_task(self):
        task = input("Enter the task: ")
        priority = input("Enter priority (high, medium, low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        new_task = {
            "task": task,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
        }

        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n===== Your Tasks =====")
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

    def mark_completed(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def remove_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f'Task "{removed_task["task"]}" removed successfully.')
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                self.remove_task()
            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
