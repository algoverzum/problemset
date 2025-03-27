// @check-accepted: *
#include <iostream>
#include <map>

using namespace std;
using ll = long long;

map<ll, ll> memo;

ll solve(ll n) {
    if (memo.count(n) == 1) {
        return memo[n];
    }
    ll ans = max(n, solve(n / 2) + solve(n / 3) + solve(n / 4));
    memo[n] = ans;
    return ans;
}

int main() {
    int t;
    cin >> t;
    memo[0] = 0;
    while (t--) {
        ll n;
        cin >> n;
        cout << solve(n) << '\n';
    }
}
