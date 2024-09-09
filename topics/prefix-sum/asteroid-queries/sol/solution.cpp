// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

// Solution with the Prefix Sum data structure.
// prefix_sum[i] = a[1] + a[2] + ... + a[i]
// The sum of consecutive elements a[l] + a[l + 1] + ... a[r]
// can be calculated with one subtraction:
// prefix_sum[r] - prefix_sum[l - 1]
// We make use of the fact that prefix_sum[0] = 0

int main() {
    ios::sync_with_stdio(false);
    int n, q;
    cin >> n >> q;
    vector<int> a(n + 1), prefix_sum(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        prefix_sum[i] = prefix_sum[i - 1] + a[i];
    }
    for (int i = 1; i <= q; i++) {
        int t, k, l, r;
        cin >> t;
        if (t == 1) {
            cin >> k;
            cout << prefix_sum[k] << '\n';
        } else {
            cin >> l >> r;
            cout << prefix_sum[r] - prefix_sum[l - 1] << '\n';
        }
    }
    return 0;
}
