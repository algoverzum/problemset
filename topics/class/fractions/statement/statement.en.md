## Fractions
Create a **Fraction** class that represents a rational number using a numerator and a denominator.

The fraction must be stored using two data members. Make these variables private (use the `__` prefix in Python or the `private` visibility modifier in C++) so they cannot be modified directly from outside the class.

* `num`: The numerator of the fraction (integer).
* `denom`: The denominator of the fraction (integer, must not be 0). The stored denominator must always be positive. `num` and `denom` must be relatively prime.

Methods (Functions):

Implement the following functions inside the class using the names given in the template:

* **Constructor:** Receives two integers (numerator and denominator). Initialize the data members and then simplify the fraction by calling `reduce()`.
* `reduce()`: Simplify the fraction using the greatest common divisor. Also ensure that the denominator is always positive.
* **String representation:** Display the fraction in the form `"numerator/denominator"`. For example: `-1/2`.
* **Addition:** Return a new fraction representing the sum of two fractions.
* **Subtraction:** Return a new fraction representing the difference of two fractions.
* **Multiplication:** Return a new fraction representing the product of two fractions.
* **Division:** Return a new fraction representing the quotient of two fractions.

Notes:

* Fractions produced by arithmetic operations must also be stored in simplified form.
* You may use the built-in `gcd` function for simplification (`math.gcd` in Python, `std::gcd` in C++).
* In C++, addition, subtraction, multiplication, division, and output can be implemented using operator overloading (`operator+`, `operator-`, `operator*`, `operator/`, `operator<<`).

### Template
Start from the provided template code. Do not modify the main program, otherwise your solution will not be accepted. You only need to implement the methods of the `Fraction` class.

### Constraints
* All values used during testing are guaranteed to be small positive integers.
* The denominator will never be 0 in the test cases.
