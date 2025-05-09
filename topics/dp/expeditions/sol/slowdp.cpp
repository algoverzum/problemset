#include <iostream>
#include <vector>
using namespace std;

struct Permit {
    int start, end, credits;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<Permit> permits(n);
    for (int i = 0; i < n; i++) {
        cin >> permits[i].start >> permits[i].end >> permits[i].credits;
    }

    vector<int> dp(m + 1, 0);

    for (int i = 1; i <= m; i++) {
        dp[i] = dp[i - 1];

        for (int j = 0; j < n; j++) {
            if (permits[j].end == i) {
                int start = permits[j].start;
                int credits = permits[j].credits;
                dp[i] = max(dp[i], dp[start - 1] + credits);
            }
        }
    }

    cout << dp[m] << endl;

    return 0;
}