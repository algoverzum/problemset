#!/usr/bin/env python3
# @check-accepted: *


class Circle:
    def __init__(self, radius):
        """Initializes self with radius"""
        self.radius = radius

    def get_radius(self):
        """Returns the radius of self"""
        return self.radius

    def set_radius(self, radius):
        """radius is a number
        Changes the radius of self to radius"""
        self.radius = radius

    def get_area(self):
        """Returns the area of self using pi = 3.14"""
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        """Returns the perimeter of self using pi = 3.14"""
        return 2 * 3.14 * self.radius

    def bigger(self, c):
        """c is a Circle object
        Returns self or c, the Circle object with the bigger radius"""
        if self.radius >= c.radius:
            return self
        else:
            return c


# Do not change anything below.
R1 = int(input())
R2 = int(input())

ok = True
try:
    C1 = Circle(R1)
    C2 = Circle(R2)
    if C1.get_radius() != R1:
        ok = False
    if abs(C1.get_area() - R1 * R1 * 3.14) > 0.01:
        ok = False
    if abs(C1.get_perimeter() - 2 * R1 * 3.14) > 0.01:
        ok = False
    if C1.bigger(C2).get_radius() != max(R1, R2):
        ok = False
    C1.set_radius(13)
    if C1.radius != 13:
        ok = False
except:
    ok = False

if ok:
    print("OK")
else:
    print("HIBA")
