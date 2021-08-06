tasksHigh = []
tasksMed = []
tasksLow = []

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

def addTask():
    task = input("What task do you need to complete?\n")
    priority = input("Is this task a high, medium, or low priority?\n")
    taskItem = {"task": task, "priority": priority}
    if priority == "high":
        tasksHigh.append(taskItem)
    elif priority == "medium":
        tasksMed.append(taskItem)
    elif priority == "low":
        tasksLow.append(taskItem)
    else:
        print("Invalid priority level. Please enter task again.")
        addTask()
    print("%s has been added successfully!\n********************" % (taskItem))
    startApp()

def viewTask():
    view = input("Would you like to view high, medium, or low priority tasks?\n")
    if view == "high":
        print("List of Tasks\n********************\n")
        counterHigh = 1
        for item in tasksHigh:
            print(counterHigh,": ", item)
            counterHigh += 1
    elif view == "medium":
        counterMed = 1
        for item in tasksMed:
            print(counterMed,": ", item)
            counterMed += 1
    elif view == "low":
        counterLow = 1
        for item in tasksLow:
            print(counterLow,": ", item)
            counterLow += 1
    else:
        print("Please enter a valid priority to view.\n")
        viewTask() 
    startApp()

def delTask():
    view = input("Would you like to delete a high, medium, or low priority task?\n")
    if view == "high":
        print("List of Tasks\n********************\n")
        counterHigh = 1
        for item in tasksHigh:
            print(counterHigh,": ", item)
            counterHigh += 1
            delete = int(input("Please select the number of the task you would like to delete.\n"))
            tasksHigh.pop(delete - 1)
    elif view == "medium":
        counterMed = 1
        for item in tasksMed:
            print(counterMed,": ", item)
            counterMed += 1
            delete = int(input("Please select the number of the task you would like to delete.\n"))
            tasksMed.pop(delete - 1)
    elif view == "low":
        counterLow = 1
        for item in tasksLow:
            print(counterLow,": ", item)
            counterLow += 1
        delete = int(input("Please select the number of the task you would like to delete.\n"))
        tasksLow.pop(delete - 1)
    else:
        print("Please enter a valid priority to delete.\n")
        delTask() 
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