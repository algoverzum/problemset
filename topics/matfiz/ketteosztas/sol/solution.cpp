// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sum = 0;
    while (n--) {
        int x;
        cin >> x;
        sum += x;
    }
    cout << (sum % 2 == 0 ? "YES\n" : "NO\n");
}
