#!/usr/bin/env python3

# Assignment comes from "100 Days of Code: The Complete Python Pro Bootcamp for 2023": https://www.udemy.com/course/100-days-of-code/ 


# Contains drinks MENU with ingredients and costs.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Contains COINS vaules in $.
COINS = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime":  0.10,
    "quarter": 0.25,
}

# Coffe machine starting resources.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# Prints report of available resources.
def report():
    print("\nPrinting report of available resources: ") 
    print(f"Water: {resources['water']}ml") 
    print(f"Milk: {resources['milk']}ml") 
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}\n")


# Asks user to enter number of inserted coins and then return their value in $.
def insert_coins():
    print("Please insert coins.")
    inserted_quarters = float(input("How many quarters? (1 quarter = 0.25$): "))
    inserted_dimes = float(input("How many dimes? (1 dime = 0.10$): "))
    inserted_nickles = float(input("How many nickles? (1 nickle = 0.05$): "))
    inserted_pennies = float(input("How many pennies? (1 penny = 0.01$): "))
    money_inserted = (inserted_quarters * COINS["quarter"]) + (inserted_dimes * COINS["dime"]) + (inserted_nickles * COINS["nickel"]) + (inserted_pennies * COINS["penny"])
    return money_inserted


# Checks whether resources are sufficient
def resources_sufficent(order_check):
    given_resource = MENU[order_check]["ingredients"]
    for resource in given_resource:
        if resources[resource] >= given_resource[resource]:
            return 0
        else:
            print(f"There is not enough {resource}")
            return 999


# Updates resources after serving.
def update_resources(chosen_drink):
    resources["money"] = resources["money"] + MENU[chosen_drink]["cost"]
    resources["water"] = resources["water"] - MENU[chosen_drink]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[chosen_drink]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[chosen_drink]["ingredients"]["coffee"]


# Checks whether enough coins were inserted, prints money in change(or money refunded) and prints serving of requested order.  
def order_result(inserted_money, chosen_drink):
    if inserted_money >= MENU[chosen_drink]["cost"]:
        money_in_change = (inserted_money - MENU[chosen_drink]["cost"])
        money_in_change = round(money_in_change, 2)
        print(f"Here is ${money_in_change} in change.")
        print(f"Here is your {chosen_drink}! Enjoy!")
        return 0
    else:
        print("You inserted not enough money.")
        print(f"Here is your money ${round(inserted_money, 2)} back.")
        return 999


# Asks user if he wants another drink and in case that not terminates program.
def should_end_func():
    end = input("Do you want to order another drink? (type 'n' if not): ").lower()
    if end == "n":
        return True
    else:
        return False
        

# Uses "while" condition to decide when to terminate program. Checks user order and calls coresponding function to check resources, refunds inserted money, completes order and decides whether terminate program. Checks for maintenance command "report" to show available resources and checks for maintenance command "off" to terminate program.
should_end = False
while should_end == False:
    print("\nWelcome to COFFEE MACHINE!")
    print("----------------------------------------------------")
    print(f"Espresso costs ${MENU['espresso']['cost']}")
    print(f"Latte costs ${MENU['latte']['cost']}")
    print(f"Cappuccino costs ${MENU['espresso']['cost']}")
    print("----------------------------------------------------\n")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if resources_sufficent(order) == 0:
            money_inserted_by_user = insert_coins()
            finall_result = order_result(money_inserted_by_user, order)
            if finall_result == 0:
                update_resources(order)
                should_end = should_end_func()
            else:
                should_end = should_end_func()
        else:
            should_end = should_end_func()
    elif order == "off":
        should_end = True
    else:
        print("Incorecct order!")
        should_end = should_end_func()
