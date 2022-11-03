from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


coffee_machine_on = True


while coffee_machine_on:
    machine_input = input("Which coffee would you like? Espresso, Latte, or Cappuccino?\n").lower()
    if machine_input == "report":
        coffee_maker.report()
        money_machine.report()

    elif machine_input == "off":
        print("Machine powering down.")
        coffee_machine_on = False

    elif machine_input == "espresso" or machine_input == "latte" or machine_input == "cappuccino":
        drink = menu.find_drink(machine_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            print(f"Sorry, there are not enough resources in the machine for this drink.\n")

    else:
        print("I'm sorry, I did not understand that.\n")
