// @check-accepted: Bsmall
// @check-runtime-error: examples NQsmall Qsmall full
#include <bits/stdc++.h>
using namespace std;

const int maxn = 64;
bool g[maxn][maxn];
bool has[maxn];

int solve(int x, int y){
    vector<int> q = {x};
    vector<int> dist(maxn, -1);
    dist[x] = 0;
    for(int i = 0; i < (int)q.size(); i++) {
        int c = q[i];
        if(c == y) return max(dist[c], 1);
        for(int j = 0; j < maxn; j++) if(has[j] && g[c][j] && dist[j] == -1) { dist[j] = dist[c] + 1; q.push_back(j); }
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);


    int n, q;
    cin>>n>>q;

    vector<int> v(n);
    for(int &x : v) {
        cin>>x;
        has[x] = true;
    }

    for(int i = 0; i < maxn; i++){
        for(int j = 0; j < maxn; j++){
            if(has[i] && has[j] && i != j && (i&j) != 0){
                g[i][j] = true;
            }
        }
    }
 
    for(int i = 0; i < q; i++){
        int x, y;
        cin>>x>>y;
        x = v[x-1];
        y = v[y-1];

        cout << (x == 0 || y == 0 ? -1 : solve(x, y)) << '\n';
    }

    return 0;
}
