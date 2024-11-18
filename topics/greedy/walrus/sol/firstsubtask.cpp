
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>
// #pragma GCC optimize("Ofast,unroll-loops")
using namespace std;
typedef long long ll;
const ll NMAX = 2e5 + 5, inf = 1e16;

void tc() {
    ll n;
    string s;
    cin >> n >> s;
    cout << "1 " << n / 2 + 1 << '\n';
}
int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t;
    cin >> t;
    while (t--)
        tc();
}
