tasks = []

def add_task():
    tasks.append(input("Enter Task : "))
    print("✅ Task Added Successfully!")

def view_task():
    print(tasks)
    if(len(tasks) == 0):
        print("No tasks available.")

def update_task():
    index = int(input("which number of task you want to update : "))
    update = input("Enter new task : ")
    tasks[index] = update
    print("✅ Task Updated Successfully!")

def remove_task():
    toRemove = int(input("Enter task number to remove : "))
    tasks.pop(toRemove-1)
    removedtask = tasks[toRemove-1]
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
            
        if(option == 1):
            numberofTask = int(input("Enter How many task you want to add : "))
            for i in range(1, numberofTask+1):
                if(option == 1):
                    add_task()
                elif(option == 2):
                    view_task()
                elif(option == 3):
                    update_task()
                elif(option == 4):
                    remove_task()
                elif(option == 5):
                    print("Closing program...")
                    break
                else:
                    print("Invaild input, please try again")
                    continue
todolist()
