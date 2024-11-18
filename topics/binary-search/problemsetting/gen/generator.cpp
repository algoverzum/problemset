#include "testlib.h"
#include <iostream>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
const ll NMAX = 1e5 + 5;
ll N[NMAX];
int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    int t = atoi(argv[1]), sumn = 2e5;
    for (ll i = 0; i < t; i++)
        sumn -= 2, N[i] += 2;
    while (sumn--)
        N[rnd.next(t)]++;

    int mina = atoi(argv[2]), maxa = atoi(argv[3]), minb = atoi(argv[4]),
        maxb = atoi(argv[5]);
    cout << t << '\n';
    for (ll i = 0; i < t; i++) {
        ll n = N[i];
        cout << n << '\n';
        for (ll j = 0; j < n; j++) {
            cout << rnd.next(mina, maxa) << " \n"[j == n - 1];
        }

        for (ll j = 0; j < n - 1; j++) {
            cout << rnd.next(minb, maxb) << " \n"[j == n - 2];
        }
    }
    return 0;
}
