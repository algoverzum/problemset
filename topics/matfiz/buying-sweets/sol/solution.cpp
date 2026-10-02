// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int X, A, B;
    cin >> X >> A >> B;

    cout << (X - A) % B << '\n';

    return 0;
}
