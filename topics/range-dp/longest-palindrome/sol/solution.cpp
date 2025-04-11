// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int longest_palindromic_subsequence(const string &word) {
    int n = word.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int i = 0; i < n; ++i)
        dp[i][i] = 1;

    for (int length = 2; length <= n; ++length) {
        for (int i = 0; i <= n - length; ++i) {
            int j = i + length - 1;

            if (word[i] == word[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[0][n - 1];
}

int main() {
    string word;
    cin >> word;
    cout << longest_palindromic_subsequence(word) << "\n";
    return 0;
}
