import menu

print("What would you like to drink?")
usrOrder = input("espresso || latte || cappuccino ")


def drink(order):
    if order == "report":
        print(menu.resources)
    else:
        water = menu.MENU[order]["ingredients"]["water"]
        coffee = menu.MENU[order]["ingredients"]["coffee"]
        if order != "espresso":
            milk = menu.MENU[order]["ingredients"]["milk"]
        else:
            milk = 0

        if menu.resources["water"] > water:
            if menu.resources["coffee"] > coffee:
                if menu.resources["milk"] > milk:
                    menu.resources["water"] -= water
                    menu.resources["coffee"] -= coffee
                    menu.resources["milk"] -= milk
                    print("Drink is ready")


drink(usrOrder)

print(menu.MENU["espresso"]["ingredients"]["water"])
