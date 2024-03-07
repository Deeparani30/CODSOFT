class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip():
            self.tasks.append(task.strip())
            print("Task added successfully!")

    def edit_task(self, index, new_text):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_text.strip()
            print("Task edited successfully!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")

    def display_tasks(self):
        print("\nCurrent Tasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        print()


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Enter the task number to edit: ")) - 1
            new_text = input("Enter the new task text: ")
            todo_list.edit_task(index, new_text)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
