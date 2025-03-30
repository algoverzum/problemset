#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;
    vector<vector<int>> v(n + 1);
    vector<int> parent(n + 1), dist(n + 1, -1);
    dist[p] = 0;
    queue<int> q;
    set<vector<int>> found_cycles;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    int mindist = n + 1, e = -1, a = -1;
    q.push(p);
    while (!q.empty()) {
        int cs = q.front();
        q.pop();
        for (int x : v[cs]) {
            if (dist[x] == -1) {
                q.push(x);
                dist[x] = dist[cs] + 1;
                parent[x] = cs;
            } else if (dist[x] >= dist[cs] &&
                       mindist > dist[x] + dist[cs] + 1) {
                mindist = dist[x] + dist[cs] + 1;
                e = x;
                a = cs;
            }
        }
    }

    if (mindist == n + 1) {
        cout << "-1";
        return 0;
    }

    int x = e, y = a;
    vector<int> path;
    path.push_back(e);
    while (x != p) {
        path.push_back(parent[x]);
        x = parent[x];
    }
    path.push_back(a);
    while (parent[y] != p) {
        path.push_back(parent[y]);
        y = parent[y];
    }

    set<int> cycle_nodes(path.begin(), path.end());
    found_cycles.insert(path);

    // cout << mindist << "\n";
    // for (int node : path) cout << node << " ";
    // cout << "\n";

    // Try to find another distinct cycle
    for (int start : cycle_nodes) {
        vector<int> new_dist(n + 1, -1), new_parent(n + 1, -1);
        queue<int> new_q;
        new_q.push(start);
        new_dist[start] = 0;

        while (!new_q.empty()) {
            int cs = new_q.front();
            new_q.pop();
            for (int x : v[cs]) {
                if (new_dist[x] == -1) {
                    new_q.push(x);
                    new_dist[x] = new_dist[cs] + 1;
                    new_parent[x] = cs;
                } else if (new_dist[x] >= new_dist[cs] && x != new_parent[cs]) {
                    vector<int> new_path;
                    int nx = x, ny = cs;
                    new_path.push_back(nx);
                    while (nx != start) {
                        new_path.push_back(new_parent[nx]);
                        nx = new_parent[nx];
                    }
                    new_path.push_back(ny);
                    while (new_parent[ny] != start) {
                        new_path.push_back(new_parent[ny]);
                        ny = new_parent[ny];
                    }
                    set<int> new_cycle_nodes(new_path.begin(), new_path.end());
                    if (new_cycle_nodes != cycle_nodes) {
                        if (new_path.size() > mindist) {
                            cout << "0";
                        } else {
                            cout << mindist << "\n";
                            for (int node : new_path)
                                cout << node << " ";
                            cout << "\n";
                        }
                        return 0;
                    }
                }
            }
        }
    }

    cout << 0;
    return 0;
}
