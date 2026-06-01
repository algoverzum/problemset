#!/usr/bin/env python3
# @check-accepted: *


class CoffeeMachine:
    def __init__(self, brand):
        """Initializes self with brand.
        Sets __is_on to False, __water_ml to 0, and __coffee_g to 0."""
        self.brand = brand
        self.__is_on = False
        self.__water_ml = 0
        self.__coffee_g = 0

    def set_electricity(self, state):
        """state is a boolean (True/False).
        Changes the power status (__is_on) of self to state."""
        self.__is_on = state

    def add_water(self, amount):
        """amount is a number.
        Adds the given amount to the machine's water level (__water_ml)."""
        self.__water_ml += amount

    def add_coffee(self, amount):
        """amount is a number.
        Adds the given amount to the machine's coffee level (__coffee_g)."""
        self.__coffee_g += amount

    def brew_coffee(self):
        """Checks if the machine is on (__is_on is True),
        has at least 50 ml water, and at least 15 g coffee.
        If all conditions are met, deducts 50 from water and 15 from coffee,
        then returns True. Otherwise, returns False."""
        if self.__is_on and self.__water_ml >= 50 and self.__coffee_g >= 15:
            self.__water_ml -= 50
            self.__coffee_g -= 15
            return True
        return False

    def get_status(self):
        """Returns a formatted string with the machine's brand,
        power status, current water, and coffee levels."""
        status = "ON" if self.__is_on else "OFF"
        return f"{self.brand} {status} {self.__water_ml}ml {self.__coffee_g}g"


# Do not change anything below.
name = input()
CM = CoffeeMachine(name)
cur = int(input())
while cur != 0:
    if cur == 2:
        on = int(input())
        if on == 1:
            CM.set_electricity(True)
        else:
            CM.set_electricity(False)
    elif cur == 3:
        water = int(input())
        CM.add_water(water)
    elif cur == 4:
        coffee = int(input())
        CM.add_coffee(coffee)
    elif cur == 5:
        CM.brew_coffee()
    elif cur == 6:
        print(CM.get_status())
    cur = int(input())
