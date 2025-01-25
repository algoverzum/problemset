#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> cells(n + 1, vector<int>(m + 1, -1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> cells[i][j];
        }
    }
    cells[n][m - 1] = 0;
    int cur;
    for (int x = m - 1; x >= 0; x--) {
        for (int y = n - 1; y >= 0; y--) {
            cur = max(cells[y + 1][x], cells[y][x + 1]);
            if (cur == -1 || cells[y][x] == -1) {
                cells[y][x] = -1;
            } else {
                cells[y][x] += max(cells[y + 1][x], cells[y][x + 1]);
            }
        }
    }

    cout << cells[0][0] << "\n";
}
