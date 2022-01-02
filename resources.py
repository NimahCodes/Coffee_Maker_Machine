class menu:
    def __init__(self, water, milk, coffee):
        self.water= water
        self.milk= milk
        self.coffee= coffee


class Resources(menu):
    ingredients = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    water = 300
    milk = 200
    coffee = 100


class espresso:
    ingredients= {
        "water": 50,
        "coffee": 18,
        "milk": 5
    }
    cost= 1.5


class latte:
    ingredients= {
        "water": 200,
        "milk": 150,
        "coffee": 24
    }
    cost= 2.5

class cappuccino:
    ingredients= {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    }
    cost=3.0




