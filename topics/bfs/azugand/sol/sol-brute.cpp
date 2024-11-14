// @check-accepted: examples NQsmall
// @check-runtime-error: Qsmall Bsmall full
#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;
bool g[maxn][maxn];
int vals[maxn];

int solve(int x, int y, int n){
    vector<int> dist(n, -1);
    vector<int> q = {x};
    dist[x] = 0;
    for(int i = 0; i < q.size(); i++){
        int a = q[i];
        if(a == y) return dist[a];
        for(int j = 0; j < n; j++){
            if(g[a][j] && dist[j] == -1){
                dist[j] = dist[a] + 1;
                q.push_back(j);
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin>>n>>q;

    for(int i = 0; i < n; i++){
        cin>>vals[i];
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(vals[i]&vals[j]){
                g[i][j] = true;
            }
        }
    }

    for(int i = 0; i < q; i++){
        int x, y;
        cin>>x>>y;
        --x, --y;
        cout << solve(x, y, n) << '\n';
    }

    return 0;
}
