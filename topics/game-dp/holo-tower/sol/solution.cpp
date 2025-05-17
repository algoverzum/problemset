// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

string holoTowerWinner(int N) {
    vector<bool> dp(N + 1, false);

    for (int i = 1; i <= N; ++i) {
        for (int move : {4, 5, 11}) {
            if (i - move >= 0 && !dp[i - move]) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[N] ? "R2-D2" : "C-3PO";
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        cout << holoTowerWinner(N) << endl;
    }

    return 0;
}
