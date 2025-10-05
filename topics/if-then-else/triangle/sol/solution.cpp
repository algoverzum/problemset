// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (a + b > c and a + c > b and b + c > a) {
        cout << 1 << '\n';
    } else {
        cout << 0 << '\n';
    }
}
