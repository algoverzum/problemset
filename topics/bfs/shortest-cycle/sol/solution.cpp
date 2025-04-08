// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;
<<<<<<< HEAD

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

=======
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
>>>>>>> b7ba10f9a7029c4d755a570a3852206d0c31c8c0
    queue<int> q;
    q.push(p);

    int min_dist = n + 1;
    int cycle_end = -1, cycle_start = -1;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
<<<<<<< HEAD

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
=======
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
>>>>>>> b7ba10f9a7029c4d755a570a3852206d0c31c8c0
                }
            }
        }
    }
    if (min_dist == n + 1) {
        cout << -1;
        return 0;
    }
<<<<<<< HEAD
    vector<int> path;
    int x = cycle_end;
=======
    int x = cycle_a, y = cycle_b;
    cout << mindist << "\n";
    vector<int> path;
    path.push_back(cycle_a);
>>>>>>> b7ba10f9a7029c4d755a570a3852206d0c31c8c0
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
<<<<<<< HEAD
    tail.push_back(p);

    cout << min_dist << "\n";

    for (int v : path)
        cout << v << " ";
    cout << cycle_start << " ";

    for (int v : tail) {
        if (v == p)
            break;
=======
    cout << cycle_b << ' ';
    while (parent[y] != p) {
        cout << parent[y] << ' ';
        y = parent[y];
>>>>>>> b7ba10f9a7029c4d755a570a3852206d0c31c8c0
    }

    return 0;
}
