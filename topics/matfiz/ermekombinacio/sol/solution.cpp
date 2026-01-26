// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;
    if (n % 2 == 0) {
        cout << "YES\n";
    } else if (k % 2 == 0 && n % 2 == 1) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
    }
    return 0;
}
