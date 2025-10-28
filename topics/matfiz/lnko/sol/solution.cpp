// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b, maradek;
    cin >> a >> b;
    do {
        maradek = a % b;
        a = b;
        b = maradek;
    } while (maradek);
    cout << a << "\n";
}
