
# Welcome to my simple coffee machine! It dispenses 3 different drinks and is coin operated (quarter, dime, nickel)
# the coffee inputs will deduct resources from the machine equal to their dictionary amounts
# coins will auto-calculate based on input and dispense change if necessary

# The special commands are as follows:
# "report" command checks the resources in the machine (water/milk/coffee/money)
# "off" turns the machine off, process terminates
# "refill" allows the user to fill up a certain resource of choice to full
# "cash out" command will dispense the money to the user
# inputting the coffee types prompted will start the transaction process

coffee = [
    {
        "espresso": {
            "water_milliliters": 50,
            "coffee_grams": 18,
            "milk_milliliters": 0,
        },
        "price_in_dollars": 1.5
    },
    {
        "latte": {
            "water_milliliters": 200,
            "coffee_grams": 24,
            "milk_milliliters": 150,
        },
        "price_in_dollars": 2.5
    },
    {
        "cappuccino": {
            "water_milliliters": 250,
            "coffee_grams": 24,
            "milk_milliliters": 100,
        },
        "price_in_dollars": 3.0
    },
]

machine_resource_levels = {
        "water": 1000,
        "milk": 1000,
        "coffee": 250,
        "money": 0.00
    }

coffee_machine_on = True
admin_password = "covfefe"


def coffee_machine_script():
    global coffee_machine_on
    machine_input = input("Which coffee would you like? Espresso, Latte, or Cappuccino?\n").lower()
    if machine_input == "report":
        print(f'''
        Water:  {machine_resource_levels["water"]}mL
        Milk:  {machine_resource_levels["milk"]}mL
        Coffee:  {machine_resource_levels["coffee"]}g
        Money:  ${machine_resource_levels["money"]}0
    ''')
    elif machine_input == "off":
        print("Machine powering down.")
        coffee_machine_on = False

    elif machine_input == "refill":
        resource_fill_type = input("What resource is being refilled? Water, Milk, or Coffee?:  ").lower()
        if resource_fill_type == "water" or resource_fill_type == "milk":
            print(f"{resource_fill_type.title()} has been refilled to 1000mL.\n")
            machine_resource_levels[resource_fill_type] = 1000
        elif resource_fill_type == "coffee":
            print(f"{resource_fill_type.title()} has been refilled to 250g.\n")
            machine_resource_levels["coffee"] = 250
        else:
            print("I did not understand that. Please retry.\n")

    elif machine_input == "cash out":
        admin_sign_in = input("Please input the admin password (Case Sensitive):  ")
        if admin_sign_in == admin_password:
            print("Access granted.")
            are_you_sure = input("Are you sure you want to cash out? Y/N:  ").lower()
            if are_you_sure == "y" or are_you_sure == "yes":
                cash_out = machine_resource_levels["money"]
                print(f"You received ${cash_out}0 from the machine.\n")
                machine_resource_levels["money"] = 0.00
            else:
                pass
        else:
            print("Access denied.\n")

    elif machine_input == "espresso" or machine_input == "latte" or machine_input == "cappuccino":
        coffee_index = 0
        if machine_input == "espresso":
            coffee_index = 0
        elif machine_input == "latte":
            coffee_index = 1
        elif machine_input == "cappuccino":
            coffee_index = 2
        price = coffee[coffee_index]["price_in_dollars"]

        if coffee[coffee_index][machine_input]["water_milliliters"] > machine_resource_levels["water"]:
            print(f"Sorry, there is not enough water in the machine for this drink.\n")
        elif coffee[coffee_index][machine_input]["milk_milliliters"] > machine_resource_levels["milk"]:
            print(f"Sorry, there is not enough milk in the machine for this drink.\n")
        elif coffee[coffee_index][machine_input]["coffee_grams"] > machine_resource_levels["coffee"]:
            print(f"Sorry, there is not enough coffee in the machine for this drink.\n")
        else:
            def calculate_change():
                print(f"\nYour drink will be ${price}0. ")
                try:
                    quarters = int(input("Quarters inserted:  "))
                    dimes = int(input("Dimes inserted:  "))
                    nickels = int(input("Nickels inserted:  "))
                    pennies = int(input("Pennies inserted:  "))
                    total_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
                    if total_inserted < price:
                        print(f"I'm sorry, that is not enough for this drink. Your ${total_inserted} have been refunded.")
                        return False
                    elif total_inserted > price:
                        if total_inserted % .1 == 0:
                            print(f"Your change is ${round(total_inserted - price, 1)}0.")
                            return True
                        else:
                            print(f"Your change is ${round(total_inserted - price, 2)}.")
                            return True
                    elif total_inserted == price:
                        return True
                except TypeError:
                    print("Use integers only please.")

            if calculate_change():
                print(f"Thank you for your patience. Please enjoy your {machine_input}. \n\n\n")
                machine_resource_levels["water"] -= coffee[coffee_index][machine_input]["water_milliliters"]
                machine_resource_levels["milk"] -= coffee[coffee_index][machine_input]["milk_milliliters"]
                machine_resource_levels["coffee"] -= coffee[coffee_index][machine_input]["coffee_grams"]
                machine_resource_levels["money"] += price
                pass
            else:
                pass

    else:
        print("I'm sorry, I did not understand that.\n")


while coffee_machine_on:
    coffee_machine_script()
