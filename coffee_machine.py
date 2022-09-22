# TODO: 1. MENU
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

# TODO: 2. resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def subtract_resources(order_ingredients, return_money):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {request} ☕️. Enjoy!")
    print(f"Your return is: ${return_money}.")


def entry(request, status):
    if request == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Income: ${income}")
    elif request == "off":
        status = "off"
        return status
    # elif request == "on":
    #     status == "on"
    #     return status
    else:
        return request


def money():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    penny = int(input("how many penny?: "))
    total_money = (quarters * 25 + dimes * 10 + nickles * 5 + penny) / 100
    total_cost = MENU[request]["cost"]
    
    return total_money - total_cost


status = "on"
income = 0
# TODO: 3. game
while status == "on":
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    entry(request, status)
    if request == "off":
        break
    elif request == "report":
        pass
    else:
        order_ingredients = MENU[request]["ingredients"]
        if check_resource(order_ingredients):
            return_money = money()
            if return_money < 0:
                print("Not Enough Money")
            else:
                subtract_resources(order_ingredients, return_money)
                income += MENU[request]["cost"]


