// @check-accepted: *
#include <algorithm>
#include <climits> // INT_MAX
#include <iostream>
#include <vector>
using namespace std;

const int INF = INT_MAX;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<pair<int, int>>> edges(N);
    for (int i = 0; i < M; ++i) {
        int U, V, W;
        cin >> U >> V >> W;
        edges[U].emplace_back(V, W);
    }

    vector<int> prev(N, INF);
    prev[0] = 0;

    for (int step = 1; step < N; ++step) {
        vector<int> curr = prev;
        for (int u = 0; u < N; ++u) {
            if (prev[u] < INF) {
                for (auto &[v, w] : edges[u]) {
                    if (prev[u] + w < curr[v]) {
                        curr[v] = prev[u] + w;
                    }
                }
            }
        }

        for (int j = 1; j < N; ++j) {
            cout << (curr[j] < INF ? curr[j] : -1) << " ";
        }
        cout << "\n";

        prev = curr;
    }

    return 0;
}
