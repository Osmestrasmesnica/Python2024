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

def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def turn_off():
    return input("Enter 'off' to turn off the Coffee Machine: ").lower() == 'off'

def print_report():
    print("Current Resource Values:")
    for resource, quantity in resources.items():
        print(f"{resource.capitalize()}: {quantity}")
    print(f"Money: ${profit:.2f}")

def check_resources(coffee_type):
    ingredients_needed = MENU[coffee_type]["ingredients"]
    for ingredient, quantity in ingredients_needed.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins(coffee_type):
    cost = MENU[coffee_type]["cost"]
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
    except ValueError:
        print("Invalid input for coins.")
        return 0

    total_coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_coins

def check_transaction(coffee_type, total_coins):
    cost = MENU[coffee_type]["cost"]
    if total_coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total_coins > cost:
        change = round(total_coins - cost, 2)
        print(f"Here is your change: ${change}")
    resources_used = MENU[coffee_type]["ingredients"]
    for ingredient, quantity in resources_used.items():
        resources[ingredient] -= quantity
    return True

profit = 0

while True:
    choice = prompt_user()

    if turn_off():
        print("Turning off the Coffee Machine. Goodbye!")
        break
    elif choice == 'report':
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            total_coins = process_coins(choice)
            if total_coins:
                if check_transaction(choice, total_coins):
                    profit += MENU[choice]["cost"]
                    print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid choice. Please choose from espresso, latte, cappuccino, or off.")
