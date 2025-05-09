// @check-accepted: *
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, s;
    cin >> n >> s;

    vector<pair<int, int>> cargo(n);
    for (int i = 0; i < n; i++) {
        cin >> cargo[i].first >> cargo[i].second;
    }

    vector<int> dp(s + 1, INT_MAX);
    dp[0] = 0;

    for (const auto &box : cargo) {
        int value = box.first;
        int weight = box.second;

        for (int i = weight; i <= s; i++) {
            if (dp[i - weight] != INT_MAX && dp[i - weight] + value < dp[i]) {
                dp[i] = dp[i - weight] + value;
            }
        }
    }

    cout << dp[s] << "\n";
    return 0;
}
