MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def sufficient_resources(choice_of_drink, available_resources):
    """Checks if the resources are sufficient for chosen drink."""
    for item in choice_of_drink["ingredients"]:
        if choice_of_drink["ingredients"][item] >= available_resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def coins():
    """Returns the total amount in $ after processing all coins."""
    print("Please insert coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total


def transaction(money, drink_cost):
    """Checks if payment is suficient."""
    global profit
    if money >= drink_cost:
        profit += drink_cost
        change = round(money-drink_cost, 2)
        print(f"Here is ${change} left.")
        return True
    else:
        print("Not enough money. Refunded")
        return False


def prepare_drink(drink_ingredients, available_resources):
    for item in available_resources:
        available_resources[item] -= drink_ingredients[item]


while True:
    print("\nWhat would you like?")
    for item in MENU:
        print(item)
    choice = input("?")
    if choice == "off":
        break
    elif choice == "report":
        print("\nAvailable resources in the Coffee Machine are:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink, resources):
            payment = coins()
            if transaction(payment, drink["cost"]):
                prepare_drink(drink["ingredients"], resources)
                print(f"Enjoy your {choice.title()}")
