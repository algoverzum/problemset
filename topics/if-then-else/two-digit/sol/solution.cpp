// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n >= 10 && n <= 99) {
        cout << 1;
    } else {
        cout << -1;
    }
    return 0;
}
