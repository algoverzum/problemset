// @check-accepted: *
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int longest_common_substring(string a, string b) {
    a = "#" + a;
    b = "$" + b;
    int n = a.length(), m = b.length();
    int max_len = 0;

    vector<vector<int>> dp(n, vector<int>(m, 0));

    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < m; ++j) {
            if (a[i] == b[j]) {
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
