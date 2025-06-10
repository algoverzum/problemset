// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> start(n), end(n), credit(n);
    vector<vector<int>> ends_at(m + 1);
    for (int i = 0; i < n; i++) {
        cin >> start[i] >> end[i] >> credit[i];
        ends_at[end[i]].push_back(i);
    }

    vector<int> dp(m + 1, 0);
    vector<int> last(m + 1, -1);
    for (int i = 1; i <= m; i++) {
        dp[i] = dp[i - 1];
        last[i] = last[i - 1];
        for (int j : ends_at[i]) {
            if (dp[i] < dp[start[j] - 1] + credit[j]) {
                dp[i] = dp[start[j] - 1] + credit[j];
                last[i] = j;
            }
        }
    }

    cout << dp.back() << "\n";
    vector<int> ans;
    int cur = last.back();
    while (cur >= 0) {
        ans.push_back(cur);
        cur = last[start[cur] - 1];
    }

    sort(ans.begin(), ans.end());
    for (int idx : ans)
        cout << idx + 1 << " ";
    cout << "\n";

    return 0;
}