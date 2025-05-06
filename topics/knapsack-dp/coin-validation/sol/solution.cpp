// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

const int MAX_X = 100000;

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> coins(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    vector<bool> dp(MAX_X + 1, false);
    dp[0] = true;
    for (int i = 0; i <= MAX_X; i++) {
        for (int coin : coins) {
            if (i - coin >= 0) {
                dp[i] = dp[i - coin] || dp[i];
            }
        }
    }
    for (int j = 0; j < q; j++) {
        int x;
        cin >> x;
        cout << (dp[x] ? "YES" : "NO") << '\n';
    }
}
