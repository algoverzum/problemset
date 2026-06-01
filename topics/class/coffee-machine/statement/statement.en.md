## Coffee Machine
Create a class called `CoffeeMachine` that simulates the operation of a coffee machine!

Data Members (Variables)  
The machine should have four attributes. The variables describing the internal state should be private (in Python, use the double underscore `__` prefix) so they cannot be modified directly from outside the class.

* `brand`: The brand of the machine (string, may be public).
* `is_on`: Indicates whether the machine has power (boolean, initially `False`).
* `water_ml`: The amount of water in the tank in milliliters (integer, initially `0`).
* `coffee_g`: The amount of coffee loaded into the machine in grams (integer, initially `0`).

Methods (Functions)  

Implement the following methods inside the class using the given names:

* The constructor. It should set the machine's brand from the parameter and initialize all other private variables to their default values (`False`/`false` and `0`).
* `set_electricity()`: Takes a boolean parameter. Sets the machine's power status (`is_on`) to the given value.
* `set_water()`: Takes a numeric parameter. Adds the given amount to the machine's current water level.
* `set_coffee()`: Takes a numeric parameter. Adds the given amount to the machine's current coffee level.
* `brew_coffee()`: Performs the coffee brewing process. Check whether the machine is turned on, contains at least 50 ml of water, and contains at least 15 g of coffee.  
  If all conditions are satisfied, deduct 50 ml of water and 15 g of coffee, then return `True`.
  If any condition is not satisfied, do not deduct anything and return `False`.
* `get_status()`: A getter method that does not modify anything. It should return a formatted string describing the current state of the machine (brand, power status as ON/OFF, water level, and coffee level).  
  Example: `"ABC ON 100ml 5g"` if the brand is `ABC`, the machine is turned on, contains 100 ml of water, and 5 g of coffee.

### Template
Start from the provided template code. Do not modify the main program, otherwise your solution will not be accepted. You only need to implement the methods of the `CoffeeMachine` class.

### Constraints
* During testing, all values are guaranteed to be small positive integers.
