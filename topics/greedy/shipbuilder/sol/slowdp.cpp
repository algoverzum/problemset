#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 100005;

int main() {
    int n;
    cin >> n;
    vector<int> deadlines(n);
    for (int i = 0; i < n; i++) {
        cin >> deadlines[i];
    }
    deadlines.insert(deadlines.begin(), 0);
    vector<vector<int>> dp(n + 1, vector<int>(MAXN, 0));
    for (int i = 1; i <= n; i++) {
        for (int day = 0; day <= n; day++) {
            dp[i][day] = max(dp[i][day], dp[i - 1][day]);
            if (day + 1 <= deadlines[i]) {
                dp[i][day + 1] = max(dp[i][day + 1], dp[i - 1][day] + 1);
            }
        }
    }
    int maxBuilt = 0, bestDay = 0;
    for (int day = 0; day <= n; day++) {
        if (dp[n][day] > maxBuilt) {
            maxBuilt = dp[n][day];
            bestDay = day;
        }
    }
    vector<int> result;
    int i = n, d = bestDay;
    while (i > 0 && d > 0) {
        if (dp[i][d] == dp[i - 1][d]) {
            i--;
        } else {
            result.push_back(i);
            i--;
            d--;
        }
    }
    reverse(result.begin(), result.end());
    cout << result.size() << endl;
    for (int idx : result)
        cout << idx << " ";
    cout << endl;
    return 0;
}
