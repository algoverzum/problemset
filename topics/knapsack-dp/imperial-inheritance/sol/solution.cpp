#include <climits>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n + 1);
    for (int i = 1; i <= n; i++)
        cin >> v[i];
    vector<vector<int>> dp(n + 1, vector<int>(20001, INT_MAX));
    vector<vector<int>> track(n + 1, vector<int>(20001));
    dp[0][10000] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= 20000; j++) {
            if (dp[i - 1][j] < INT_MAX) {
                if (dp[i - 1][j] < dp[i][j + v[i]]) {
                    dp[i][j + v[i]] = dp[i - 1][j];
                    track[i][j + v[i]] = 1;
                }
                if (dp[i - 1][j] < dp[i][j - v[i]]) {
                    dp[i][j - v[i]] = dp[i - 1][j];
                    track[i][j - v[i]] = -1;
                }
                if (dp[i - 1][j] + v[i] < dp[i][j]) {
                    dp[i][j] = dp[i - 1][j] + v[i];
                    track[i][j] = 0;
                }
            }
        }
    }
    cout << dp[n][10000] << '\n';
    vector<int> ans;
    int x = 1e4;
    for (int i = n; i; i--) {
        if (track[i][x] == 1) {
            cout << i << ' ';
            x -= v[i];
        } else if (track[i][x] == -1) {
            ans.push_back(i);
            x += v[i];
        }
    }
    cout << '\n';
    for (int i : ans)
        cout << i << ' ';
    cout << '\n';
}