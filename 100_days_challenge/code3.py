# A TO-DO LIST

def view_task(tasks):
    if not tasks:
        print("your list is empty")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def add_task(tasks):
    data = input("Enter task: ")
    
    tasks.append(data)
    print(F"{data} has been added to the list")

def remove_task(tasks):
    view_task(tasks)
    task_num = int(input("select a number to remove"))
    if 0 < task_num < len(tasks):
        remove = tasks.pop(task_num -1)
        print(f"{remove}, has been removed from your list")
    else:
        print("invalid input")


tasks = []

while True:
    print("\n1. view task \n2. add task \n3. remove task\n4. exit")
    choice = int(input("Enter a number: "))

    if choice == 1:
        view_task(tasks)
    elif choice == 2:
        add_task(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("invalid input, try again")