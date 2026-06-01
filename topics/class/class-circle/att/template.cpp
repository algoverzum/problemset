#include <cmath>
#include <iostream>
using namespace std;

class Circle {
  private:
    int radius;

  public:
    // Initialize this circle object with r radius
    Circle(int r) {
        // Write your code here
    }

    // Returns the radius of this circle
    int get_radius() {
        // Write your code here
    }

    // Changes the radius of this circle to r
    void set_radius(int r) {
        // Write your code here
    }

    // Returns the area of this circle using pi = 3.14
    double get_area() {
        // Write your code here
    }

    // Returns the perimeter of this circle using pi = 3.14
    double get_perimeter() {
        // Write your code here
    }

    // Returns the Circle object with the bigger radius, this or c
    Circle bigger(Circle c) {
        // Write your code here
    }
};

// Do not change anything below.
int main() {
    int R1, R2;
    cin >> R1 >> R2;

    bool ok = true;

    Circle C1(R1);
    Circle C2(R2);

    if (C1.get_radius() != R1)
        ok = false;

    if (fabs(C1.get_area() - 3.14 * R1 * R1) > 0.01)
        ok = false;

    if (fabs(C1.get_perimeter() - 2 * 3.14 * R1) > 0.01)
        ok = false;

    if (C1.bigger(C2).get_radius() != max(R1, R2))
        ok = false;

    C1.set_radius(13);

    if (C1.get_radius() != 13)
        ok = false;

    if (ok)
        cout << "OK\n";
    else
        cout << "ERROR\n";

    return 0;
}
