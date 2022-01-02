class CoffeeDispenser:
    def __init__(self):
        self.ingredients = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def resource_report(self):
        print(f"Water: {self.ingredients['water']}")
        print(f"Milk: {self.ingredients['milk']}")
        print(f"coffee: {self.ingredients['coffee']}")


    answer=''

    def is_available(self, coffee_flavor):
        test= True
        for key in self.ingredients:
            if coffee_flavor.ingredients[key] > self.ingredients[key]:
                print(f"We are low on {key}")
                test= False
                quit()
        return test

    def coffee_processing(self, choice_flavor):
        for item in self.ingredients:
            self.ingredients[item] -= choice_flavor.ingredients[item]

