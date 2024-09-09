// @check-accepted: examples small
// @check-time-limit-exceeded: big
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n, q;
    cin >> n >> q;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    for (int i = 1; i <= q; i++) {
        int t, k, l, r;
        cin >> t;
        if (t == 1) {
            cin >> k;
            cout << accumulate(a.begin() + 1, a.begin() + k + 1, 0) << '\n';
        } else {
            cin >> l >> r;
            cout << accumulate(a.begin() + l, a.begin() + r + 1, 0) << '\n';
        }
    }
    return 0;
}
