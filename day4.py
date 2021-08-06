def mainMenu():
    message ="""
Main Menu:\n
Press 1 to add a task
Press 2 to view all tasks
Press 3 to delete a task
Press q to quit
********************
"""
    print(message)

tasks = []

def addTask():
    task = input("What task do you need to complete?\n")
    priority = input("Is this task a high, medium, or low priority?\n")
    taskItem = {"task": task, "priority": priority}
    if priority == "high" or "medium" or "low":
        tasks.append(taskItem)
    else:
        print("Invalid priority level. Please enter task again.")
        addTask()
    print("%s has been added successfully!\n********************" % (taskItem))
    startApp()

def viewTask():
    print("List of Tasks\n********************\n")
    counter = 1
    for item in tasks:
        print(counter,": ", item)
        counter += 1
    startApp()

def delTask():
    print("List of Tasks\n********************\n")
    counter = 1
    for item in tasks:
        print(counter,": ", item)
        counter += 1
    delete = int(input("Please select the number of the task you would like to delete.\n"))
    tasks.pop(delete - 1)
    startApp()

def startApp():
    mainMenu()
    while True:
        action = input("Please select a menu option.\n********************\n")
        if action == "1":
            addTask()
        elif action == "2":
            viewTask()
        elif action == "3":
            delTask()
        elif action == "q":
            exit()
        else:
            print("********************\nPlease enter a valid menu option.\n********************")
            mainMenu()
        
startApp()