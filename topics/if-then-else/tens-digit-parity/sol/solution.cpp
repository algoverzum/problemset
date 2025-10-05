// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, jegy;
    cin >> n;
    jegy = n / 10 % 10;
    if (jegy % 2 == 0) {
        cout << 1 << "\n";
    } else {
        cout << 0 << "\n";
    }
}
