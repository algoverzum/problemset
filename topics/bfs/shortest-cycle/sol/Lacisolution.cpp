#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;
    vector<vector<int>> g(n + 1);
    vector<int> parent(n + 1), dist(n + 1, -1), subtree(n + 1, -1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> b >> a;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    int mindist = n + 1;
    int cycle_a = -1, cycle_b = -1;
    dist[p] = 0;
    queue<int> q;
    q.push(p);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int to : g[cur]) {
            if (dist[to] == -1) {
                q.push(to);
                dist[to] = dist[cur] + 1;
                parent[to] = cur;
                if (cur == p)
                    subtree[to] = to;
                else
                    subtree[to] = subtree[cur];
            } else {
                if (subtree[to] != subtree[cur] && dist[to] >= dist[cur] &&
                    mindist > dist[to] + dist[cur] + 1) {
                    mindist = dist[to] + dist[cur] + 1;
                    cycle_a = to;
                    cycle_b = cur;
                }
            }
        }
    }
    if (mindist == n + 1) {
        cout << "-1";
        return 0;
    }
    int x = cycle_a, y = cycle_b;
    cout << mindist << "\n";
    vector<int> path;
    path.push_back(cycle_a);
    while (x != p) {
        path.push_back(parent[x]);
        x = parent[x];
    }
    for (int i = path.size() - 1; i >= 0; i--) {
        cout << path[i] << " ";
    }
    cout << cycle_b << ' ';
    while (parent[y] != p) {
        cout << parent[y] << ' ';
        y = parent[y];
    }
    return 0;
}