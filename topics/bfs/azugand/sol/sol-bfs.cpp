// @check-accepted: examples NQsmall Qsmall
// @check-time-limit-exceeded: Bsmall full
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin>>n>>q;

    vector<int> v(n);
    for(int &x : v) cin>>x;

    for(int i = 0; i < q; i++){
        int x, y;
        cin>>x>>y;
        x = v[x-1];
        y = v[y-1];
        int ans = 1;
        bool ok = true;
        while((x&y) == 0 && ok) {
            ok = false;
            int nxt = x;
            for(int z : v){
                if((z&x) != 0 && (z&x) != z){
                    ok = true;
                    nxt |= z;
                }
            }
            x = nxt;
            ans++;
        }
        cout << ((x&y) == 0 ? -1 : ans) << '\n';
    }

    return 0;
}
