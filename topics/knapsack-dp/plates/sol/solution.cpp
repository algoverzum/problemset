// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, K, P;
        cin >> N >> K >> P;

        vector<vector<int>> prefix(N, vector<int>(K + 1, 0));

        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= K; j++) {
                int x;
                cin >> x;
                prefix[i][j] = prefix[i][j - 1] + x;
            }
        }

        vector<vector<int>> dp(N + 1, vector<int>(P + 1, 0));

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= P; j++) {
                for (int x = 0; x <= min(j, K); x++) {
                    dp[i][j] =
                        max(dp[i][j], dp[i - 1][j - x] + prefix[i - 1][x]);
                }
            }
        }

        cout << dp[N][P] << '\n';
    }

    return 0;
}
