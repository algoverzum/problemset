#include <climits>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

const int INF = INT_MAX;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<pair<int, int>>> adj(N + 1);

    for (int i = 0; i < M; i++) {
        int U, V, W;
        cin >> U >> V >> W;
        adj[U].emplace_back(V, W);
    }

    vector<int> dist(N + 1, INF);
    dist[1] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>>
        pq; // Min-heap: {distance, node}
    pq.emplace(0, 1);

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u])
            continue;

        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.emplace(dist[v], v);
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        if (dist[i] == INF) {
            cout << "X ";
        } else {
            cout << dist[i] << " ";
        }
    }

    cout << "\n";
    return 0;
}