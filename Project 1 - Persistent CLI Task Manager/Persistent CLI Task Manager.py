import json
# Global Variables
tasks = []

# Functions
def main_menu():
    options = ["View Tasks", "Add Task", "Mark Task as Completed", "Change Task Priority", "Delete Task", "Exit"]

    while True:
        print("=== Task Manager ===")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        try:
            choice = int(input(f"Enter your choice (1-{len(options)}): "))
        except ValueError:
            print("Error: Invalid input! Please enter a number")
            continue
        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_task_as_complete()
        elif choice == 4:
            change_task_priority()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}")
            continue

def view_tasks(only_view = False):
    if len(tasks) == 0:
        print("No Tasks Found!")
    else:
        print("-----------------------------------------------------------")
        print(f"{'ID':^4}| {'Status':^12} | {'Priority':^10} | {'Title':^26}")
        print("-----------------------------------------------------------")
        for i, task in enumerate(tasks, start=1):
            print(f"{i:^4}| {('Completed' if task['status'] else 'Pending'):^12} | {task['priority']:^10} | {task['task']}")
        print("-----------------------------------------------------------")
    if(only_view == False):
        goto_mainmenu()
    
def add_task():
    task_title = input("Enter task title: ")
    while True:
        if task_title == "":
            print("Error: Task cannot be empty")
            task_title = input("Enter task title again: ")
            continue
        else:
            priority = input("Enter priority (high/medium/low): ").lower()
            if priority not in ["high", "medium", "low"]:
                print("Error: Invalid priority")
                continue
            else:
                tasks.append({
                    "status": False,
                    "priority": priority,
                    "task": task_title
                })
                write_to_file()
                print(f"Task '{task_title}' added successfully with '{priority}' priority")
                break
    goto_mainmenu()

def mark_task_as_complete():
    view_tasks(True)
    if len(tasks) != 0:
        found = False

        for i, task in enumerate(tasks, start=1):
            if task['status'] == True:
                continue
            else:
                found = True
                break

        if not found:
            print("No incomplete tasks found!")
            goto_mainmenu()
            return
            
        while True:
            try:
                index = int(input("Enter task ID to mark as complete (0 to cancel): "))
                if index == 0:
                    break
                if index < 0 or index > len(tasks):
                    print("Error: Invalid task ID")
                    continue
                elif tasks[index - 1]['status'] == True:
                    print("Error: Task is already completed")
                    continue
                else:
                    tasks[index - 1]['status'] = True
                    write_to_file()
                    print(f"Task '{tasks[index - 1]['task']}' marked as complete")
                    break
            except ValueError:
                print("Error: Invalid input! Please enter a number")
                continue
    goto_mainmenu()

def change_task_priority():
    view_tasks(True)
    if len(tasks) != 0:
        while True:
            try:
                index = int(input("Enter task ID to change priority (0 to cancel): "))
                if index == 0:
                    break
                if index < 0 or index > len(tasks):
                    print("Error: Invalid task ID")
                    continue
                elif tasks[index - 1]['status'] == True:
                    print("Error: Cannot change priority of a completed task")
                    continue
                else:
                    priority = input("Enter new priority (high/medium/low): ").lower()
                    if priority not in ["high", "medium", "low"]:
                        print("Error: Invalid priority")
                        continue
                    else:
                        tasks[index - 1]['priority'] = priority
                        write_to_file()
                        print(f"Task '{tasks[index - 1]['task']}' priority changed to '{priority}'")
                        break
            except ValueError:
                print("Error: Invalid input! Please enter a number")
                continue
    goto_mainmenu()

def delete_task():
    view_tasks(True)
    if len(tasks) != 0:
        while True:
            try:
                index = int(input("Enter task ID to delete (0 to delete all | -1 to cancel): "))
                if index == -1:
                    break
                if index == 0:
                    tasks.clear()
                    write_to_file()
                    print("All tasks deleted")
                    break
                
                if index < 0 or index > len(tasks):
                    print("Error: Invalid task ID")
                    continue
                else:
                    task = tasks[index - 1]['task']
                    tasks.pop(index - 1)
                    write_to_file()
                    print(f"Task '{task}' deleted successfully")
                    break
            except ValueError:
                print("Error: Invalid input! Please enter a number")
                continue
    goto_mainmenu()

def goto_mainmenu():
    key = input("Press 'm' to return to main menu: ").lower()
    if key == "m":
        return
    else:
        print("Invalid choice! Please press 'm' to return to main menu")
        goto_mainmenu()

def write_to_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Main
try:
    file = open("tasks.json", "r")
    tasks = json.load(file)
    file.close()
except (FileNotFoundError, json.JSONDecodeError):
    write_to_file()
    
main_menu()