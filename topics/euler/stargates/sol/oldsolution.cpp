// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void bfs(int start, vector<vector<int>> &adj, vector<bool> &visited) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v]) {
            if (!visited[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
    }
}

bool euler(int n, vector<vector<int>> &adj) {
    vector<bool> visited(n, false);
    int start = -1;
    for (int i = 0; i < n; i++) {
        if (!adj[i].empty()) {
            start = i;
            break;
        }
    }
    if (start == -1)
        return true;
    bfs(start, adj, visited);
    for (int i = 0; i < n; i++) {
        if (!adj[i].empty() && !visited[i])
            return false;
    }
    for (int i = 0; i < n; i++) {
        if (adj[i].size() % 2 != 0)
            return false;
    }
    return true;
}

int main() {
    int n, r;
    cin >> n >> r;
    n++;
    vector<vector<int>> adj(n);
    for (int i = 0; i < r; i++) {
        int v1, v2;
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }
    cout << (euler(n, adj) ? "YES" : "NO") << "\n";
    return 0;
}