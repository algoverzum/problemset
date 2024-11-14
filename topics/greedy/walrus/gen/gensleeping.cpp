#include "testlib.h"

#include <iostream>
#include <utility>
#include <vector>
#include <cmath>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
const ll NMAX=1e5+5;
ll N[NMAX];
int main(int argc, char* argv[]) {
    registerGen(argc,argv,1);
    int t=atoi(argv[1]),sumn=3e5;
    for(ll i=0;i<t;i++)
        sumn--,N[i]++;
    while(sumn--) N[rnd.next(t)]++;
    cout<<t<<'\n';
    for(ll i=0;i<t;i++){
        ll n=N[i];
        cout<<n<<'\n';
        for(ll j=0;j<n;j++){
            cout<<".";
        }
        cout<<'\n';
    }
    return 0;
}

