// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b, c, ans = -1;

    cin >> a >> b >> c;
    for (int i = 1; i < 10000; i++) {
        if (i % 5 == a and i % 7 == b and i % 11 == c) {
            ans = i;
            break;
        }
    }
    cout << ans << "\n";
    return 0;
}
