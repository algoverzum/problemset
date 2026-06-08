#!/usr/bin/env python3
# @check-accepted: *

from math import gcd


class Fraction:
    """
    A number represented as a fraction
    """

    def __init__(self, num, denom):
        """num and denom are integers"""
        assert type(num) == int and type(denom) == int, "ints not used"
        assert denom != 0, "denominator cannot be zero"

        self.__num = num
        self.__denom = denom
        self.reduce()

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
        """Reduce fraction to lowest terms"""
        g = gcd(self.__num, self.__denom)

        self.__num //= g
        self.__denom //= g

        # Keep denominator positive
        if self.__denom < 0:
            self.__num *= -1
            self.__denom *= -1

    def __str__(self):
        """Returns a string representation of self"""
        return f"{self.__num}/{self.__denom}"

    def __add__(self, other):
        """Returns a new fraction representing the addition"""
        top = self.__num * other.__denom + self.__denom * other.__num
        bott = self.__denom * other.__denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """Returns a new fraction representing the subtraction"""
        top = self.__num * other.__denom - self.__denom * other.__num
        bott = self.__denom * other.__denom
        return Fraction(top, bott)

    def __mul__(self, other):
        """Returns a new fraction representing the multiplication"""
        return Fraction(self.__num * other.__num, self.__denom * other.__denom)

    def __truediv__(self, other):
        """Returns a new fraction representing the division"""
        return Fraction(self.__num * other.__denom, self.__denom * other.__num)

    def __float__(self):
        """Returns a float value of the fraction"""
        return self.__num / self.__denom

    def inverse(self):
        """Returns a new fraction representing 1/self"""
        return Fraction(self.__denom, self.__num)


a, b, c, d = [int(x) for x in input().split()]
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
