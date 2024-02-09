#To-Do List
#Class whith the different functions on what the user wants to do 
class TodoList:
 def __init__(self):
     self.tasks = []

 def add_task(self, task):
     self.tasks.append(task)
     print(f'Task"{task}" added.')

 def remove_task(self,task):
     if task in self.tasks:
         self.tasks.remove(task)
         print(f'Task"{task}"removed.')
     else:
         print (f'Task "{task}"not found.')
 def show_tasks(self):
     if not self.tasks:
        print("No tasks on the list.")
     else:
         print("Tasks:")
         for index, task in enumerate(self.tasks, start = 1):
             print(f'{index}.{task}')
def main():
    todo_list = TodoList()
    while True:
        print("\nOptions:")
        print("1. Add Tasks")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            task = input("Enter the task:")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            print("Existing the todo list. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
                         