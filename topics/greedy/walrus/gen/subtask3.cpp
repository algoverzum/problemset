#include "testlib.h"

#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
const ll NMAX = 1e5 + 5;
ll N[NMAX];
int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    int t = atoi(argv[1]), maxn = atoi(argv[2]), p = atoi(argv[3]);
    for (ll i = 0; i < t; i++)
        N[i] = maxn;
    cout << t << '\n';
    for (ll i = 0; i < t; i++) {
        ll n = N[i];
        cout << n << '\n';
        int c = rnd.next(2);
        for (ll j = 0; j < n; j++) {
            if (!rnd.next(p))
                c ^= 1;
            cout << ".-"[c];
        }
        cout << '\n';
    }
    return 0;
}
