from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuu=Menu()
checker=CoffeeMaker()
mchecker=MoneyMachine()

print(menuu.get_items())
order = input("What would you like for drink?")

dor = menuu.find_drink(order)
if(dor != "None"):
    if checker.is_resource_sufficient(dor)==True:
        if mchecker.make_payment(dor.cost):
            # ask for cash n check if it's suff or not'
            checker.make_coffee(dor)
            print(checker.report())
            print(mchecker.report())