#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }
    vector<vector<pair<int, int>>> dp(
        n + 2, vector<pair<int, int>>(m, make_pair(-100, -1)));
    for (int i = 1; i < n + 1; i++) {
        dp[i][0].first = grid[i - 1][0];
        dp[i][0].second = i;
    }
    for (int j = 1; j < m; j++) {
        for (int i = 1; i < n + 1; i++) {
            if (dp[i - 1][j - 1].first > dp[i][j - 1].first &&
                dp[i - 1][j - 1].first > dp[i + 1][j - 1].first) {
                dp[i][j] = dp[i - 1][j - 1];
                dp[i][j].first += grid[i - 1][j];
            } else if (dp[i][j - 1].first > dp[i - 1][j - 1].first &&
                       dp[i][j - 1].first > dp[i + 1][j - 1].first) {
                dp[i][j] = dp[i][j - 1];
                dp[i][j].first += grid[i - 1][j];
            } else {
                dp[i][j] = dp[i + 1][j - 1];
                dp[i][j].first += grid[i - 1][j];
            }
        }
    }
    pair<int, int> maximal = dp[1][m - 1];
    for (int i = 1; i < n + 1; i++) {
        if (dp[i][m - 1].first > maximal.first) {
            maximal = dp[i][m - 1];
        }
    }
    cout << maximal.first << "\n" << maximal.second << "\n";
}
