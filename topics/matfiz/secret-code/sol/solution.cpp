// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, a, b, c, db = 0, k = 1;
    bool volt = false;

    cin >> n >> a >> b >> c;
    for (int i = 1; i <= n; i++)
        k = k * 10;
    for (int i = 1; i < k; i++) {
        if (i % 5 == a and i % 7 == b and i % 11 == c) {
            if (not volt)
                cout << i << endl;
            db++;
            volt = true;
        }
    }
    if (db > 0)
        cout << db << "\n";
    else
        cout << -1 << "\n";
    return 0;
}
