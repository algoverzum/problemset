// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (a % 2 == b % 2 && b % 2 == c % 2) {
        cout << "NO" << "\n";
    } else {
        cout << "YES" << "\n";
    }
}
