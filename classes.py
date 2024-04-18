class CoffeeDrink:
    def __init__(self, coffee=0.0, water=0.0, milk_foam=0.0, steamed_milk=0.0, chocolate=0.0):
        self.__coffee = coffee
        self.__water = water
        self.milk_foam = milk_foam
        self.steamed_milk = steamed_milk
        self.chocolate = chocolate

    def make_espresso(self):
        print("Espresso made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.0
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_mocha(self):
        print("Mocha made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.1

    def make_macchiato(self):
        print("Macchiato made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_latte(self):
        print("Latte made")
        self.__coffee = 0.1
        self.__water = 0.1
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.0

    def make_americano(self):
        print("Americano made")
        self.__coffee = 0.1
        self.__water = 0.1
        self.milk_foam = 0.0
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_cappuccino(self):
        print("Cappuccino made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.0

    def add_coffee(self, amount):
        self.__coffee += amount

    def add_water(self, amount):
        self.__water += amount

    def add_milk_foam(self, amount):
        self.milk_foam += amount

    def add_steamed_milk(self, amount):
        self.steamed_milk += amount

    def add_chocolate(self, amount):
        self.chocolate += amount

    def remove_milk_foam(self):
        print("Removing milk foam")
        self.milk_foam = 0.0

    def __del__(self):
        print("Coffee drink destroyed")

    def __str__(self):
        if self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate == 0:
            return "Cappuccino"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam == 0 and self.steamed_milk == 0 and self.chocolate == 0:
            return "Espresso"
        elif self.__coffee > 0 and self.__water > 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate == 0:
            return "Latte"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate > 0:
            return "Mocha"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk == 0 and self.chocolate == 0:
            return "Macchiato"
        else:
            return "Unknown Coffee Drink"

def main():
    my_coffee = CoffeeDrink()
    
    my_coffee.make_espresso()
    print(f"Current drink: {my_coffee}")
    
    my_coffee.make_latte()
    print(f"Current drink: {my_coffee}")

    my_coffee.remove_milk_foam()
    my_coffee.make_cappuccino()
    print(f"Current drink: {my_coffee}")

    my_coffee.make_mocha()
    print(f"Current drink: {my_coffee}")

    my_coffee.add_milk_foam(0.2)
    my_coffee.add_steamed_milk(0.1)
    
    del my_coffee

main()
