// @check-accepted: N1
// @check-wrong-answer: examples
// @check-zero: NMsmall Nsmall no-limits
/**
 *    author:  BERNARD B.01
 **/
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt;
    cin >> tt;
    while (tt--) {
        int n, m;
        cin >> n >> m;
        string s;
        cin >> s;
        if (m <= 2) {
            cout << 0 << '\n';
            continue;
        }
        array<array<int, 2>, 2> dp;
        for (int f1 : {0, 1}) {
            for (int f2 : {0, 1}) {
                dp[f1][f2] = f1 + f2;
            }
        }
        const int inf = int(1e9) + 9;
        for (int i = 2; i < m; i++) {
            array<array<int, 2>, 2> new_dp;
            for (int f1 : {0, 1}) {
                for (int f2 : {0, 1}) {
                    new_dp[f1][f2] = inf;
                }
            }
            for (int f1 : {0, 1}) {
                for (int f2 : {0, 1}) {
                    for (int f3 : {0, 1}) {
                        if ((s[i - 2] ^ f1) == (s[i - 1] ^ f2) &&
                            (s[i - 1] ^ f2) == (s[i] ^ f3)) {
                            continue;
                        }
                        new_dp[f2][f3] = min(new_dp[f2][f3], f3 + dp[f1][f2]);
                    }
                }
            }
            swap(dp, new_dp);
        }
        int ans = inf;
        for (int f1 : {0, 1}) {
            for (int f2 : {0, 1}) {
                ans = min(ans, dp[f1][f2]);
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
