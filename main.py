
from resources import cappuccino, latte, espresso
from Coffee_maker import CoffeeDispenser
from MoneyMachine import Sales
coffee_maker= CoffeeDispenser()
money_machine= Sales()
while True:
    option = str(input("What would you like”? (espresso/latte/cappuccino): ")).strip().lower()
    if option == "off":
        print("Shutting Down")
        print("")
        quit()
    elif option == 'report':
        coffee_maker.resource_report()
        money_machine.profit_report()
    elif option == "latte":
        option = latte()
        aval_resource= coffee_maker.is_available(option)
        sufficient_money= money_machine.is_sufficient_money(option)
        if aval_resource:
            if sufficient_money:
                print("Here's your Hot espresso")
                coffee_maker.coffee_processing(option)
    elif option=='espresso':
        option= espresso()
        aval_resource = coffee_maker.is_available(option)
        sufficient_money = money_machine.is_sufficient_money(option)
        if aval_resource:
            if sufficient_money:
                print("Here's your Hot espresso")
                coffee_maker.coffee_processing(option)
    elif option == "cappuccino":
        option= cappuccino()
        aval_resource = coffee_maker.is_available(option)
        sufficient_money = money_machine.is_sufficient_money(option)
        if aval_resource:
            if sufficient_money:
                print("Here's your Hot espresso")
                coffee_maker.coffee_processing(option)
    else:
        print("Invalid Coffee flavor")












