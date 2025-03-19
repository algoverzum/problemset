// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, e, a, p;
    cin >> n >> m >> p;
    vector<vector<int>> v(n + 1);
    vector<int> parent(n + 1), dist(n + 1, -1);
    dist[p] = 0;
    queue<int> q;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> b >> a;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int mindist = n + 1;
    q.push(p);
    while (!q.empty()) {
        int cs = q.front();
        q.pop();
        for (int x : v[cs]) {
            if (dist[x] == -1) {
                q.push(x);
                dist[x] = dist[cs] + 1;
                parent[x] = cs;
            } else {
                if (dist[x] >= dist[cs] && mindist > dist[x] + dist[cs] + 1) {
                    mindist = dist[x] + dist[cs] + 1;
                    e = x;
                    a = cs;
                }
            }
        }
    }
    if (mindist == n + 1) {
        cout << "-1";
        return 0;
    }
    int x = e, y = a;
    cout << mindist << "\n";
    vector<int> path;
    path.push_back(e);
    while (x != p) {
        path.push_back(parent[x]);
        x = parent[x];
    }
    for (int i = path.size() - 1; i >= 0; i--) {
        cout << path[i] << " ";
    }
    cout << a << ' ';
    while (parent[y] != p) {
        cout << parent[y] << ' ';
        y = parent[y];
    }
    return 0;
}