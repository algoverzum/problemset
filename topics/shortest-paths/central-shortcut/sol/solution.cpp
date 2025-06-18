// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            cin >> dist[i][j];
            if (dist[i][j] == -1)
                dist[i][j] = INF;
        }

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (i != j)
                dist[i][j] = min(dist[i][0] + dist[0][j], dist[i][j]);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << (dist[i][j] == INF ? -1 : dist[i][j]);
            if (j + 1 < n)
                cout << " ";
        }
        cout << "\n";
    }
    return 0;
}
