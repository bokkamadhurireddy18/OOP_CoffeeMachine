from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker= CoffeeMaker()
menu= Menu()
money_machine= MoneyMachine()

def choose():
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == 'off':  # only for maintainers
        return False
    elif choice == 'report':  # only for maintainers
        coffee_maker.report()
        money_machine.report()
        return True
    else:
        drink= menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        return True

order= True
while order:
    order = choose()
