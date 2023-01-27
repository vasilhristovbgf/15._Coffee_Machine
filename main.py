import menu
import time
import os
import art
import sys

repeat = True

def checkRes(a, b, c, order):
    """water, coffee, milk, order"""
    for i in range(4):
        time.sleep(0.5)
        print("Checking resources " + str(), end="\r", flush=True)
    resources = True


    #Check water:
    if menu.resources["water"] < a:
        print("Error: Not Enough Water")
        if input("Please type *reload* to add water: ") == "reload":
            menu.resources["water"] = 300
            print("Water reloaded successfully! ")
        else:
            print("No water has been added. ")
            resources = False

    #Check coffee:
    if menu.resources["coffee"] < b:
        print("Error: Not Enough Coffee")
        if input("Please type *reload* to add coffee: ") == "reload":
            menu.resources["coffee"] = 300
            print("Coffee reloaded successfully! ")
        else:
            print("No coffee has been added. ")
            resources = False

    #Check milk:
    if menu.resources["milk"] < c:
        print("Error: Not Enough Milk")
        if input("Please type *reload* to add milk: ") == "reload":
            menu.resources["milk"] = 300
            print("Milk reloaded successfully! ")
        else:
            print("No milk has been added. ")
            resources = False

    if resources == False:

        print("Not enough resources, please try again! ")
        goOn = input("Press *Enter* to Continue...")

    return resources

def askMoney(item):
    price = menu.MENU[item]["cost"]
    money = 0
    #while money < price:
    while True:
        try:
            money += 0.25*float(input("How many quarters? "))
            break
        except:
            print("Please only input numbers..")
            continue

    while True:
        try:
            money += 0.10*float(input("How many dimes? "))
            break
        except:
            print("Please only input numbers..")
            continue

    while True:
        try:
            money += 0.05*float(input("How many nickels? "))
            break
        except:
            print("Please only input numbers..")
            continue

    while True:
        try:
            money += 0.01*float(input("How many pennies? "))
            break
        except:
            print("Please only input numbers..")
            continue

    print(f"Total: {money}")
    if len(menu.resources) == 3:
        menu.resources["income"] = money

    if money == price:
        menu.resources["income"] += money
        return money
    elif money > price:
        print(f"Here's your change: {round(money-price, 2)}")
        money = price
        menu.resources["income"] += money
        return money
    elif money < price:
        print(f"Not enough money inserted. Here is your change: {round(money, 2)}")
        print("Please try again")
        goOn = input("Press *Enter* to continue...")

def main():
    os.system("cls")

    #global usrOrder
    print("What would you like to drink?")
    usrOrder = input("espresso 1.50$ || latte 2.50$ || cappuccino 3.00$ ")

    if usrOrder == "off":
        print("Goodbye!")
        time.sleep(2)
        os.system("cls")
        global repeat
        repeat = False
        return repeat
    elif usrOrder == "report":
        os.system("cls")
        for i in menu.resources:
            print(f"{i}: {menu.resources[i]}")
        goOn = input("Press *Enter* to continue...")
    else:
        water = menu.MENU[usrOrder]["ingredients"]["water"]
        coffee = menu.MENU[usrOrder]["ingredients"]["coffee"]
        if usrOrder != "espresso":
            milk = menu.MENU[usrOrder]["ingredients"]["milk"]
        elif usrOrder == "espresso":
            milk = 0

#MAKE DRINK
        price = menu.MENU[usrOrder]["cost"]
        if checkRes(water, coffee, milk, usrOrder):
            if askMoney(usrOrder) == price:
                menu.resources["water"] -= water
                menu.resources["coffee"] -= coffee
                menu.resources["milk"] -= milk
                for i in range(4):
                    time.sleep(0.5)
                    print("Preparing " + str(3-i), end="\r", flush=True)
                time.sleep(0.5)
                print("Drink is ready")
                print(art.drink)
                time.sleep(2)
                os.system("cls")

        # else:
        #     if input("Please type *reload* to reload the machine: ") == "reload":
        #         menu.resources["water"] = 300
        #         menu.resources["coffee"] = 100
        #         menu.resources["milk"] = 200
        #         print("Machine reloaded successfully! ")
        #         goOn = input("Press *Enter* to Continue... ")

while repeat == True:
    main()
