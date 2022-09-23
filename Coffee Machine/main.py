# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


def print_report(resources, profit):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")


def check_resources(choice, current_resources, profit):
    resources = current_resources
    requested_resources = MENU[choice]['ingredients']
    enough_resources = True

    for ingredient in requested_resources:
        request_amount = requested_resources[ingredient]
        current_resource = resources[ingredient]
        if (current_resource - request_amount) > 0:
            resources[ingredient] = current_resource - request_amount
        else:
            print(f"Sorry you don't have enough {ingredient}")
            enough_resources = False
        # TODO 4: Check resources sufficient?
        if enough_resources:

            # TODO 5: Process Coins
            money = get_coins()
            cost = MENU[choice]["cost"]
            change = money - cost

            # TODO 6: Check if transaction is successful
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
                return current_resources, profit
            else:
                profit = MENU[choice]['cost'] + profit
                if change > 0:
                    print(f"Here is your change: ${change}")
                # TODO 7: Make Coffee
                print(f"Here is your {choice}! Enjoy")
                return resources, profit
        else:
            return current_resources, profit


def get_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def start_coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    user_request = ""
    profit = 0
    # TODO: 1. b) The prompt should show every time action has completed
    while user_request != "off":
        # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
        user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO: 1.a) Check the user's input to decide what to do next
        if user_request == 'report':
            # TODO: 3. Print copy of resources
            print_report(resources, profit)
        # TODO 2: Check if the coffee machine is turned off
        elif user_request == "off":
            break
        else:
            resources, profit = check_resources(user_request, resources, profit)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_coffee_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
