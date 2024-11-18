#include <iostream>
// #pragma GCC optimize("Ofast,unroll-loops")
using namespace std;
typedef long long ll;
const ll NMAX = 2e5 + 5, inf = 1e16;
ll a[NMAX], b[NMAX];
void tc() {
    ll n, ans = 1e9;
    cin >> n;
    for (ll i = 1; i <= n; i++) {
        cin >> a[i];
        ans = min(ans, a[i]);
    }
    for (ll i = 1; i < n; i++)
        cin >> b[i];

    cout << ans << '\n';
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t;
    cin >> t;
    while (t--)
        tc();
}
