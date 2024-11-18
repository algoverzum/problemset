#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        long long a, b, k;
        cin >> a >> b >> k;

        long long ans = 0;
        for (long long i = 0; i <= k; i++) {
            ans = max(ans, gcd(a + i, b + k - i));
        }

        cout << ans << '\n';
    }

    return 0;
}
