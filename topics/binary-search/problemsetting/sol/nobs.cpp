#include <iostream>
// #pragma GCC optimize("Ofast,unroll-loops")
using namespace std;
typedef long long ll;
const ll NMAX = 2e5 + 5, NMAX2 = 2.4e7 + 5, inf = 1e16;
ll a[NMAX], b[NMAX];
ll cpyb[NMAX];
bool ok(ll n, ll target) {
    for (ll i = 1; i < n; i++)
        cpyb[i] = b[i];
    cpyb[0] = cpyb[n] = 0;
    for (ll i = 1; i <= n; i++) {
        ll curr = target - a[i] - cpyb[i - 1];
        if (curr > 0) {
            cpyb[i] -= curr;
            if (cpyb[i] < 0) {
                return false;
            }
        }
    }
    return true;
}
void tc() {
    ll n;
    cin >> n;
    for (ll i = 1; i <= n; i++)
        cin >> a[i];

    for (ll i = 1; i < n; i++)
        cin >> b[i];

    for (ll ans = 1;; ans++) {
        if (!ok(n, ans)) {
            cout << ans - 1 << '\n';
            return;
        }
    }
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
