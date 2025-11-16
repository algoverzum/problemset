// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int speed, altitude;
    cin >> speed >> altitude;
    while (speed > 1 and altitude > 0) {
        cout << speed << " " << altitude << "\n";
        speed -= 10;
        altitude -= 2;
    }
    return 0;
}
