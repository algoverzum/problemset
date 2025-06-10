// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<array<int, 3>> request(n);
    vector<vector<int>> ends_at(m + 1);
    int idx = 0;
    for (auto &[start, end, credit] : request) {
        cin >> start >> end >> credit;
        ends_at[end].push_back(idx++);
    }

    vector<int> dp(m + 1, 0);
    vector<int> last(m + 1, -1);
    for (int i = 1; i <= m; i++) {
        dp[i] = dp[i - 1];
        last[i] = last[i - 1];
        for (int j : ends_at[i]) {
            auto &[start, end, credit] = request[j];
            if (dp[i] < dp[start - 1] + credit) {
                dp[i] = dp[start - 1] + credit;
                last[i] = j;
            }
        }
    }

    cout << dp.back() << "\n";
    vector<int> ans;
    int cur = last.back();
    while (cur >= 0) {
        ans.push_back(cur);
        cur = last[request[cur][0] - 1];
    }

    sort(ans.begin(), ans.end());
    for (int &idx : ans)
        cout << idx + 1 << " ";

    return 0;
}