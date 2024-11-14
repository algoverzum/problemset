#include "testlib.h"

#include <iostream>
#include <utility>
#include <vector>
#include <cmath>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
const ll NMAX=1e5+5;
int main(int argc, char* argv[]) {
    registerGen(argc,argv,1);
    int maxn=atoi(argv[1]);
    int t=(2<<maxn)-2-maxn;
    cout<<t<<'\n';
    for(ll n=1;n<=maxn;n++){
        for(ll msk=0;msk<(1<<n)-1;msk++){
            
            cout<<n<<'\n';
            for(ll i=0;i<n;i++)
                cout<<".-"[msk>>i&1];
            cout<<'\n';
        }
    }
    return 0;
}

