#!/usr/bin/env python3


class CoffeeMachine:
    def __init__(self, brand):
        """Initializes self with brand.
        Sets __is_on to False, __water_ml to 0, and __coffee_g to 0."""
        # Write your code here

    def set_electricity(self, state):
        """state is a boolean (True/False).
        Changes the power status (__is_on) of self to state."""
        # Write your code here

    def set_water(self, amount):
        """amount is a number.
        Adds the given amount to the machine's water level (__water_ml)."""
        # Write your code here

    def set_coffee(self, amount):
        """amount is a number.
        Adds the given amount to the machine's coffee level (__coffee_g)."""
        # Write your code here

    def brew_coffee(self):
        """Checks if the machine is on (__is_on is True),
        has at least 50 ml water, and at least 15 g coffee.
        If all conditions are met, deducts 50 from water and 15 from coffee,
        then returns True. Otherwise, returns False."""
        # Write your code here

    def get_status(self):
        """Returns a formatted string with the machine's brand,
        power status, current water, and coffee levels."""
        # Write your code here


# Do not change anything below.
name = input()
CM = CoffeeMachine(name)
ok = True
try:
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
            CM.set_water(water)
        elif cur == 4:
            coffee = int(input())
            CM.set_coffee(coffee)
        elif cur == 5:
            CM.brew_coffee()
        elif cur == 6:
            print(CM.get_status())
        cur = int(input())
except:
    ok = False

if ok:
    print("OK")
else:
    print("HIBA")
