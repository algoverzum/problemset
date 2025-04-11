// @check-accepted: examples small
// @check-time-limit-exceeded: all
// O(n^3)
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int longest_common_substring(const string &s1, const string &s2) {
    int m = s1.length(), n = s2.length();
    int max_len = 0;

    // Check all pairs (i, j)
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int len = 0;
            while (i + len < m && j + len < n && s1[i + len] == s2[j + len]) {
                len++;
            }
            max_len = max(max_len, len);
        }
    }

    return max_len;
}

int main() {
    string word1, word2;
    cin >> word1 >> word2;

    cout << longest_common_substring(word1, word2) << endl;

    return 0;
}
