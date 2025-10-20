// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n % 3 == 0) {
        cout << 1 << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
