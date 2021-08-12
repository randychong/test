def mainMenu():
    message ="""
Main Menu:\n
----------------------------------------\n
Press 1 to add a shopping list
Press 2 to view all shopping lists
Press 3 to add grocery items to a list
Press q to quit
****************************************\n
"""
    print(message)

shoppingList = []

def addList():
    store = input("store?\n")
    address = input("address?\n")
    list = {"store": store, "address": address, "items": []}
    shoppingList.append(list)
    print("|%s - %s| has been added successfully!" % (store, address))
    startApp()

def viewList():
    print(shoppingList)

def addItemToList():
    counter = 1
    for list in shoppingList:
        print(counter, "-", list)
        counter += 1
    choice = int(input("Which list would you like to add to? Please select the number.\n"))
    item = input("Which item would you like to add?\n")
    price = input("How much is it?\n")
    quantity = input("How many do you need?\n")
    itemToAdd = {item, price, quantity}
    shoppingList[choice - 1]["items"].append(itemToAdd)

def startApp():
    mainMenu()
    action = input("Please select a menu option.\n")
    if action == "1":
        addList()
        startApp()
    elif action == "2":
        viewList()
        startApp()
    elif action == "3":
        addItemToList()
        startApp()
    elif action == "q":
        exit()
    else:
        print("Please enter a valid menu option.\n")
        startApp()
        
startApp()