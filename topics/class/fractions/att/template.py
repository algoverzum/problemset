#!/usr/bin/env python3


class Fraction:
    """
    A number represented as a fraction
    """

    def __init__(self, num, denom):
        """num and denom!=0 are integers
        call reduce here"""
        # Write your code here

    # Getters
    def get_num(self):
        return self.__num

    def get_denom(self):
        return self.__denom

    # Setters
    def set_num(self, value):
        assert type(value) == int, "numerator must be an int"
        self.__num = value
        self.reduce()

    def set_denom(self, value):
        assert type(value) == int, "denominator must be an int"
        assert value != 0, "denominator cannot be zero"
        self.__denom = value
        self.reduce()

    def reduce(self):
        """Reduce fraction to lowest terms
        Keep denominator positive"""
        # Write your code here

    def __str__(self):
        """Returns a string representation of self
        For example '-1/2' if numerator = -1 and denominator = 2"""
        # Write your code here

    def __add__(self, other):
        """Returns a new fraction representing the addition"""
        # Write your code here

    def __sub__(self, other):
        """Returns a new fraction representing the subtraction"""
        # Write your code here

    def __mul__(self, other):
        """Returns a new fraction representing the multiplication"""
        # Write your code here

    def __truediv__(self, other):
        """Returns a new fraction representing the division"""
        # Write your code here

    def __float__(self):
        """Returns a float value of the fraction"""
        return self.__num / self.__denom


# Do not change anything below.

f1 = Fraction(a, b)
f2 = Fraction(c, d)

print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
f1.set_num(60)
print(f1)
print(f1.get_num(), f1.get_denom())
