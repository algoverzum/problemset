// @check-accepted: *
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main() {
    int n, sum = 0;
    cin >> n;
    vector<int> weights(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> weights[i];
        sum += weights[i];
    }

    int target = sum / 2;
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1));
    dp[0][0] = true;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= target; j++) {
            dp[i][j] =
                dp[i - 1][j] || (j >= weights[i] && dp[i - 1][j - weights[i]]);
        }
    }

    int left = target;
    while (!dp[n][left]) {
        --left;
    }

    vector<bool> left_cargo(n, false);
    int left_cnt = 0;
    int j = left;
    for (int i = n; i > 0; i--) {
        if (!dp[i - 1][j]) {
            left_cargo[i] = true;
            left_cnt++;
            j -= weights[i];
        }
    }

    cout << sum - 2 * left << "\n";
    cout << left_cnt;
    for (int i = 1; i <= n; i++)
        if (left_cargo[i])
            cout << " " << i;
    cout << "\n";
    cout << n - left_cnt;
    for (int i = 1; i <= n; i++)
        if (!left_cargo[i])
            cout << " " << i;
    cout << "\n";

    return 0;
}
