// @check-accepted: *
#include <cmath>
#include <iostream>
using namespace std;

class Circle {
  public:
    int radius;

    Circle(int radius) { this->radius = radius; }

    int get_radius() { return radius; }

    void set_radius(int radius) { this->radius = radius; }

    double get_area() { return 3.14 * radius * radius; }

    double get_perimeter() { return 2.0 * 3.14 * radius; }

    Circle *bigger(Circle *c) {
        if (radius >= c->radius)
            return this;
        else
            return c;
    }
};

// Do not change anything below.
int main() {
    int R1, R2;
    cin >> R1 >> R2;

    bool ok = true;

    try {
        Circle C1(R1);
        Circle C2(R2);

        if (C1.get_radius() != R1)
            ok = false;

        if (fabs(C1.get_area() - 3.14 * R1 * R1) > 0.01)
            ok = false;

        if (fabs(C1.get_perimeter() - 2 * 3.14 * R1) > 0.01)
            ok = false;

        if (C1.bigger(&C2)->get_radius() != max(R1, R2))
            ok = false;

        C1.set_radius(13);

        if (C1.radius != 13)
            ok = false;
    } catch (...) {
        ok = false;
    }

    if (ok)
        cout << "OK\n";
    else
        cout << "HIBA\n";

    return 0;
}
