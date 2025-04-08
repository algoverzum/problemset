// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;

    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> b >> a;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    vector<int> parent(n + 1, -1);
    vector<int> dist(n + 1, -1);
    vector<int> branch(n + 1, -1);
    dist[p] = 0;
    branch[p] = p;

    queue<int> q;
    q.push(p);

    int min_dist = n + 1;
    int cycle_end = -1, cycle_start = -1;
    while (!q.empty()) {
        int cs = q.front();
        q.pop();

        for (int x : graph[cs]) {
            if (dist[x] == -1) {
                parent[x] = cs;
                dist[x] = dist[cs] + 1;
                branch[x] = (cs == p) ? x : branch[cs];
                q.push(x);
            } else {
                if (x == parent[cs])
                    continue;
                if (branch[cs] != branch[x]) {
                    if (dist[x] >= dist[cs] &&
                        min_dist > dist[x] + dist[cs] + 1) {
                        min_dist = dist[x] + dist[cs] + 1;
                        cycle_end = x;
                        cycle_start = cs;
                    }
                }
            }
        }
    }
    if (min_dist == n + 1) {
        cout << -1;
        return 0;
    }
    vector<int> path;
    int x = cycle_end;
    while (x != p) {
        path.push_back(x);
        x = parent[x];
    }
    path.push_back(p);
    reverse(path.begin(), path.end());

    vector<int> tail;
    x = cycle_start;
    while (x != p) {
        tail.push_back(x);
        x = parent[x];
    }
    tail.push_back(p);

    cout << min_dist << "\n";

    for (int v : path)
        cout << v << " ";
    cout << cycle_start << " ";

    for (int v : tail) {
        if (v == p)
            break;
    }

    return 0;
}
