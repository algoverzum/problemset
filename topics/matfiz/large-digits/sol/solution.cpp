// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int A = a / 100 + (a / 10) % 10 + a % 10;
    int B = b / 100 + (b / 10) % 10 + b % 10;

    if (A > B)
        cout << A << '\n';
    else
        cout << B << '\n';

    return 0;
}
