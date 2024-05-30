
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task})
        print(f'Added task: "{task}"')

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f'Task "{task["task"]}" deleted.')
        else:
            print(f'Task {task_number} does not exist.')

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")

    def list_tasks(self):
        return


def print_menu():
    print("ToDo List Menu")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Clear All Tasks")
    print("4. Exit")


def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '3':
            todo_list.clear_tasks()
        elif choice == '4':
            print("Exiting the ToDo List application.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
