#include <iostream>
//#pragma GCC optimize("Ofast,unroll-loops")
using namespace std;
typedef long long ll;
const ll NMAX=2e5+5,inf=1e16;
ll a[NMAX],b[NMAX];
void tc(){
    ll n;
    cin>>n;
    for(ll i=1;i<=n;i++){
        cin>>a[i];
    }
    for(ll i=1;i<n;i++)
        cin>>b[i];
    b[0]=b[n]=a[0]=0;
    for(ll i=1;i<=n;i++){
        if(a[i]) continue;
        if(b[i-1]) continue;
        if(b[i]){
            b[i]--;
            continue;
        }
        cout<<"0\n";
        return;
    }
    cout<<"1\n";
}
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    ll t; cin>>t; while(t--)
        tc();
}
