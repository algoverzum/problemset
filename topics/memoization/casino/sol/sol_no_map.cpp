// @check-accepted: *
#include <iostream>

using namespace std;
using ll = long long;

const int LIMIT = 10000000;

ll dp[LIMIT];

ll solve(ll n) {
    if (n < LIMIT && dp[n] != -1) {
        return dp[n];
    }
    ll ans = max(n, solve(n / 2) + solve(n / 3) + solve(n / 4));
    if (n < LIMIT) {
        dp[n] = ans;
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < LIMIT; i++) {
        dp[i] = -1;
    }
    dp[0] = 0;
    while (t--) {
        ll n;
        cin >> n;
        cout << solve(n) << '\n';
    }
}
