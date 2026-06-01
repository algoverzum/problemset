#include <cmath>
#include <iostream>
using namespace std;

class Circle {
  private:
    int radius;

  public:
    Circle(int r) {
        // Initialize this with radius
        // Write your code here
    }

    int get_radius() {
        // Returns the radius of this
        // Write your code here
    }

    void set_radius(int r) {
        // Changes the radius of this to r
        // Write your code here
    }

    double get_area() {
        // Returns the area of this using pi = 3.14
        // Write your code here
    }

    double get_perimeter() {
        // Returns the perimeter of this using pi = 3.14
        // Write your code here
    }

    Circle bigger(Circle c) {
        // Returns this or c, the Circle object with the bigger radius
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
