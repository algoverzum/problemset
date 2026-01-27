// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;
    if (n % 2 == 0) {
        cout << "YES\n";
    } else if (k % 2 == 1 && n >= k) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}
