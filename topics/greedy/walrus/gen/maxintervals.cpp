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
    int t = atoi(argv[1]), n = atoi(argv[2]);
    // int t=3,n=16;
    cout << t << '\n';
    for (ll i = 0; i < t; i++) {
        cout << n << '\n';
        if (rnd.next(2))
            for (ll j = 0; j < n / 5; j++)
                cout << "-.-..";
        else
            for (ll j = 0; j < n / 5; j++)
                cout << ".-..-";
        cout << '\n';
    }
    return 0;
}
