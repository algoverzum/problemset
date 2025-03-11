// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int N, M, deg[201], vis[201];
vector<int> g[201];

void dfs(int u) {
    vis[u] = 1;
    for (int v : g[u]) {
        if (!vis[v])
            dfs(v);
    }
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        deg[u]++;
        deg[v]++;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs(1);
    for (int u = 1; u <= N; u++) {
        if (deg[u] % 2 || !vis[u] && deg[u]) {
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
}
