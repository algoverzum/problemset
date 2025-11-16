// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    const int S = 1000;
    const int M = 2000;
    int speed, altitude;
    cin >> speed >> altitude;
    int lepesszam = 0;
    while (speed < S && altitude <= M) {
        speed += 2;
        altitude += 4;
        lepesszam++;
    }
    cout << lepesszam << endl;
    return 0;
}
