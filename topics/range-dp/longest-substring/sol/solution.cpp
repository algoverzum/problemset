// @check-accepted: *
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int longest_common_substring(const string &s1, const string &s2) {
    int m = s1.length(), n = s2.length();
    int max_len = 0;

    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                max_len = max(max_len, dp[i][j]);
            }
        }
    }

    return max_len;
}

int main() {
    string word1, word2;
    cin >> word1 >> word2;

    cout << longest_common_substring(word1, word2) << "\n";

    return 0;
}
