// @check-accepted: *
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (a > b) { // swap(a, b);
        a = a + b;
        b = a - b;
        a = a - b;
    }
    if (a == 0) {
        return b;
    }
    return gcd(a, b - a);
}

// Do not change anything below.
int main() {
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << "\n";
}
