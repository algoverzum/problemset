// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, szum = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cout << i << " ";
            szum = szum + i;
        }
    }
    if (szum == 2 * n)
        cout << 1 << "\n";
    else
        cout << 0 << "\n";
}
