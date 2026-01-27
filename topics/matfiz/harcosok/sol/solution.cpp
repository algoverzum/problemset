// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> warrior(n);
    for (int i = 0; i < n; ++i) {
        cin >> warrior[i];
    }

    sort(warrior.begin(), warrior.end());

    int ans = 0;
    for (int i = 1; i < n; i += 2) {
        ans += warrior[i] - warrior[i - 1];
    }

    cout << ans << '\n';
    return 0;
}
