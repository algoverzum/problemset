#include <bits/stdc++.h>
using namespace std;

// A number represented as a fraction in reduced form.
// The denominator is always positive;
// the sign of the fraction is carried by the numerator.
class Fraction {
  private:
    int num;
    int denom;

    // Reduce fraction to lowest terms
    // Keep denominator positive
    void reduce() {
        // Write your code here
    }

  public:
    // num and denom!=0 are integers
    // call reduce here
    Fraction(int n, int d) {
        // Write your code here
    }

    // Getters
    int get_num() const { return num; }

    int get_denom() const { return denom; }

    // Setters
    void set_num(int value) {
        num = value;
        reduce();
    }

    void set_denom(int value) {
        assert(value != 0);

        denom = value;
        reduce();
    }

    double to_double() const { return (double)num / denom; }

    // Operator overloading
    // Returns a new fraction representing the addition
    Fraction operator+(const Fraction &other) const {
        // Write your code here
    }

    // Returns a new fraction representing the subtraction
    Fraction operator-(const Fraction &other) const {
        // Write your code here
    }

    // Returns a new fraction representing the multiplication
    Fraction operator*(const Fraction &other) const {
        // Write your code here
    }

    // Returns a new fraction representing the division
    Fraction operator/(const Fraction &other) const {
        // Write your code here
    }

    // Returns a string representation of this fraction
    // For example '-1/2' if numerator = -1 and denominator = 2
    friend ostream &operator<<(ostream &os, const Fraction &f) {
        // Write your code here
    }
};

// Do not change anything below.
int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    Fraction f1(a, b);
    Fraction f2(c, d);

    cout << f1 << endl;
    cout << f2 << endl;
    cout << f1 + f2 << endl;
    cout << f1 - f2 << endl;
    cout << f1 * f2 << endl;
    cout << f1 / f2 << endl;

    f1.set_num(60);

    cout << f1 << endl;
    cout << f1.get_num() << " " << f1.get_denom() << endl;

    return 0;
}
