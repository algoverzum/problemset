// @check-accepted: *
#include <iostream>
using namespace std;

long long summa(int a, int b) {
    if (a == b) {
        return a;
    }
    return b + summa(a, b - 1);
}

// Do not change anything below.
int main() {
    int a, b;
    cin >> a >> b;
    cout << summa(a, b) << "\n";
}
