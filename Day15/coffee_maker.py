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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_transaction_successful(money_received, cost):
    '''return true if payment is accepted or false if insufficient'''
    if money_received > cost:
        change = round(money_received - cost, 2)
        print(f"Your change is ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def check_resource(order_resources):
    for item in order_resources:
        if order_resources[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def process_funds():
    '''return total calculation of funds'''
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickel?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_resources):
    '''Dedect the requitred ingredients from the resources'''
    for item in order_resources:
        resources[item] -= order_resources[item]
    print(f"Here is your {drink_name}")
    
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            payment = process_funds()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])

