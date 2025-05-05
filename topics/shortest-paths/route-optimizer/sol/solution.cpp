// @check-accepted: *
#include <climits>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

const int INF = INT_MAX;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<tuple<int, int, int>> edges;

    for (int i = 0; i < M; i++) {
        int U, V, W;
        cin >> U >> V >> W;
        edges.emplace_back(U, V, W);
    }

    vector<int> dist(N + 1, INF);
    dist[1] = 0;

    for (int i = 0; i < N - 1; i++) {
        for (auto [U, V, W] : edges) {
            if (dist[U] != INF && dist[U] + W < dist[V]) {
                dist[V] = dist[U] + W;
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
