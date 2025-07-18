tasks = []
def addTasks():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully")

def viewTasks():
    if not tasks:
        print("No tasks to display")
    else:
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")  
def deleteTask():
    viewTasks()
    taskToDelete = int(input("Enter the task to delete: "))
    if taskToDelete < len(tasks) and taskToDelete >= 0:
        tasks.pop(taskToDelete)
        print(f"Task #{taskToDelete} deleted successfully")
    else:
        print("Invalid task number")
          
if __name__ == '__main__':

    print("Welcome to the To-Do-List App")
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if (choice == "1"):
          addTasks()
        elif (choice == "2"): 
          deleteTask()
        elif (choice == "3"):
          viewTasks()
        elif (choice == "4"):
          break
        else:
          print("Invalid Choice")

        

