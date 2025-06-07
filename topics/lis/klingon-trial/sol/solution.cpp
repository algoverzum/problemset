// @check-accepted: *

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> T(n);
    for (int i = 0; i < n; ++i) {
        cin >> T[i];
    }

    vector<int> dp(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (T[j] < T[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int max_length = dp[0];
    for (int i = 1; i < n; ++i) {
        max_length = max(max_length, dp[i]);
    }

    cout << max_length << endl;

    return 0;
}
