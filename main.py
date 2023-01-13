import menu

print("What would you like to drink?")
order = input("1. Espresso || 2. Latte || 3. Cappuccino ")
def espresso():
    water = menu.MENU["espresso"]["ingredients"]["water"]
    coffee = menu.MENU["espresso"]["ingredients"]["coffee"]

def latte():
    water = menu.MENU["latte"]["ingredients"]["water"]
    coffee = menu.MENU["latte"]["ingredients"]["coffee"]
    milk = menu.MENU["latte"]["ingredients"]["milk"]

def cappuccino():
    water = menu.MENU["cappuccino"]["ingredients"]["water"]
    coffee = menu.MENU["cappuccino"]["ingredients"]["coffee"]
    milk = menu.MENU["cappuccino"]["ingredients"]["milk"]



print(menu.MENU["espresso"]["ingredients"]["water"])