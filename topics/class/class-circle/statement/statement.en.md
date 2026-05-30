## Circle Class
Complete the methods of the `Circle` class!

A circle has a single data attribute: its radius. The class should allow the radius to be queried and modified, compute the area and perimeter of the circle, and compare two circles.

Requirements:

* The constructor should store the radius of the circle.
* The `get_radius()` method should return the radius of the circle.
* The `set_radius()` method should update the radius of the circle.
* The `get_area()` method should compute the area of the circle using the formula: $A = 3.14 \cdot r^2$. (That is, use $3.14$ as the value of $\pi$.)
* The `get_perimeter()` method should compute the circumference of the circle using the formula: $C = 2 \cdot 3.14 \cdot r$. (That is, use $3.14$ as the value of $\pi$.)
* The `bigger()` method should return the `Circle` object with the larger radius. If the radii are equal, either object may be returned.

### Template
Start from the provided template code. Do not modify the main program, otherwise your solution will not be accepted. You only need to implement the methods of the `Circle` class.

### Constraints
* $1 \le r \le 10^6$
