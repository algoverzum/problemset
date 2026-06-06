// @check-accepted: *
#include <iostream>
#include <numeric>
#include <stdexcept>

using namespace std;

class Fraction {
  private:
    int num;
    int denom;

    void reduce() {
        int g = gcd(num, denom);

        num /= g;
        denom /= g;

        if (denom < 0) {
            num *= -1;
            denom *= -1;
        }
    }

  public:
    Fraction(int n, int d) {
        if (d == 0)
            throw invalid_argument("Denominator cannot be zero");

        num = n;
        denom = d;
        reduce();
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
        if (value == 0)
            throw invalid_argument("Denominator cannot be zero");

        denom = value;
        reduce();
    }

    Fraction inverse() const { return Fraction(denom, num); }

    double toDouble() const { return static_cast<double>(num) / denom; }

    // Operator overloading
    Fraction operator+(const Fraction &other) const {
        int top = num * other.denom + denom * other.num;
        int bott = denom * other.denom;
        return Fraction(top, bott);
    }

    Fraction operator-(const Fraction &other) const {
        int top = num * other.denom - denom * other.num;
        int bott = denom * other.denom;
        return Fraction(top, bott);
    }

    Fraction operator*(const Fraction &other) const {
        return Fraction(num * other.num, denom * other.denom);
    }

    Fraction operator/(const Fraction &other) const {
        return Fraction(num * other.denom, denom * other.num);
    }

    friend ostream &operator<<(ostream &os, const Fraction &f) {
        os << f.num << "/" << f.denom;
        return os;
    }
};

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
