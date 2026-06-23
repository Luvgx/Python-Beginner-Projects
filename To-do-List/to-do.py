tasks = []

def add_task(number1):
    for i1 in range(number1):
        tasks.append(input(f"Enter task {i1+1} :"))
        print("✅ Task Added Successfully!")

def view_task():
    if(len(tasks) == 0):
        print("No tasks available.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

def update_task():
    if(len(tasks) == 0):
        print("No tasks available.")
    else:
        print("================================")
        index = int(input("Enter task number to update : "))
        if(index > len(tasks)):
            print("Invalid task number!")
        elif(index <= 0):
            print("Invalid task number!")
        else:
            update = input("Enter new task : ")
            tasks[index-1] = update
            print("✅ Task Updated Successfully!")

def remove_task():
    if(len(tasks) == 0):
        print("📋 No tasks available.\nAdd a task first!")
    else:
        toRemove = int(input("Enter task number to remove : "))
        if(toRemove > len(tasks)):
            print("Invalid task number!")
        elif(toRemove < 1):
            print("Invalid task number!")
        else:
            removedtask = tasks.pop(toRemove-1)
            # removedtask = tasks[toRemove-1]
            print(removedtask ,"Removed Successfully!")

def todolist():
    while True:
        print("\n================================")
        print("          TO-DO-LIST         ")
        print("================================\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update task")
        print("4. Remove Task")
        print("5. Exit")
        option = int(input("Choose an option : "))
        print("---------------------------------")
            
        if(option == 1):
            numberofTask = int(input("\nEnter number of tasks you want to add : "))
            if(numberofTask <= 0):
                print("Please enter at least 1 task.")
                continue
            add_task(numberofTask)
        elif(option == 2):
            view_task()
        elif(option == 3):
            view_task()
            update_task()
        elif(option == 4):
            view_task()
            remove_task()
        elif(option == 5):
            print("\n================================")
            print("Thank you for using To-Do List!\nGoodbye 👋")
            print("================================\n")
            break
        else:
            print("\n================================")
            print("Invaild input, please try again")
            print("================================\n")
            continue
todolist()
