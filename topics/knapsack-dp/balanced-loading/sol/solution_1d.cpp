// @check-accepted: *
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> weights(n);
    for (int i = 0; i < n; ++i) {
        cin >> weights[i];
    }

    int total = accumulate(weights.begin(), weights.end(), 0);
    vector<bool> dp(total + 1, false);
    vector<int> prev(total + 1, -1);

    dp[0] = true;

    for (int t = 0; t < n; ++t) {
        for (int i = total; i >= weights[t]; --i) {
            if (dp[i - weights[t]] && !dp[i]) {
                dp[i] = true;
                prev[i] = t;
            }
        }
    }

    int left = total / 2;
    while (left >= 0 && !dp[left]) {
        --left;
    }

    vector<bool> used(n, false);
    int curr = left;
    while (curr > 0) {
        int task = prev[curr];
        used[task] = true;
        curr -= weights[task];
    }

    vector<int> left_cargo, right_cargo;
    for (int i = 0; i < n; ++i) {
        if (used[i]) {
            left_cargo.push_back(i + 1);
        } else {
            right_cargo.push_back(i + 1);
        }
    }

    cout << abs(total - 2 * left) << "\n";
    cout << left_cargo.size() << " ";
    for (int idx : left_cargo)
        cout << idx << " ";
    cout << "\n";
    cout << right_cargo.size() << " ";
    for (int idx : right_cargo)
        cout << idx << " ";
    cout << "\n";

    return 0;
}
