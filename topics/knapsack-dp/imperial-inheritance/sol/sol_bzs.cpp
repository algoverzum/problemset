// Igazságos osztozkodás.cpp : This file contains the 'main' function. Program
// execution begins and ends there.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n + 1, 0);
    for (int i = 1; i <= n; i++)
        cin >> v[i];
    vector<vector<int>> dp(n + 1, vector<int>(2e4 + 1, 1e5));
    vector<vector<int>> vf(n + 1, vector<int>(2e4 + 1, 0));
    dp[0][1e4] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= 2e4; j++) {
            dp[i][j] = dp[i - 1][j] + v[i];
            if (j >= v[i] && dp[i - 1][j - v[i]] < dp[i][j]) {
                dp[i][j] = dp[i - 1][j - v[i]];
                vf[i][j] = v[i];
            }
            if (j <= 2e4 - v[i] && dp[i - 1][j + v[i]] < dp[i][j]) {
                dp[i][j] = dp[i - 1][j + v[i]];
                vf[i][j] = -v[i];
            }
        }
    }
    vector<int> ans1;
    vector<int> ans2;
    int j = 1e4;
    for (int i = n; i > 0; i--) {
        if (vf[i][j] > 0)
            ans1.push_back(i);
        if (vf[i][j] < 0)
            ans2.push_back(i);
        j -= vf[i][j];
    }
    cout << dp[n][1e4] << endl;
    for (int i : ans1)
        cout << i << " ";
    cout << endl;
    for (int i : ans2)
        cout << i << " ";
    cout << endl;
}
