from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    choice = input(f"What would you like? ({menu.get_items()}report): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        if not (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)) : 
            continue
        coffee_maker.make_coffee(drink)

