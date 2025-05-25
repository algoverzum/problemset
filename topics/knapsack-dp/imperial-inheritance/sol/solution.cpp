// @check-accepted: *
#include <array>
#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> V(N);
    int total = 0;
    for (int i = 0; i < N; i++) {
        cin >> V[i];
        total += V[i];
    }
    int M = total, OFFSET = M;
    // dp[d] = max total_assigned with difference d-OFFSET
    vector<int> dp(2 * M + 1, -INF), ndp(2 * M + 1);
    // to reconstruct:
    // par[d] = 0,1,2 for leave/A/B
    vector<int> par(N * (2 * M + 1));

    dp[OFFSET] = 0;
    for (int i = 0; i < N; i++) {
        fill(ndp.begin(), ndp.end(), -INF);
        int v = V[i];
        for (int d = 0; d <= 2 * M; d++) {
            if (dp[d] < 0)
                continue;
            // 1) leave unassigned
            if (dp[d] > ndp[d]) {
                ndp[d] = dp[d];
                par[i * (2 * M + 1) + d] = 0;
            }
            // 2) to brother1 (difference +v)
            if (d + v <= 2 * M && dp[d] + v > ndp[d + v]) {
                ndp[d + v] = dp[d] + v;
                par[i * (2 * M + 1) + d + v] = 1;
            }
            // 3) to brother2 (difference −v)
            if (d - v >= 0 && dp[d] + v > ndp[d - v]) {
                ndp[d - v] = dp[d] + v;
                par[i * (2 * M + 1) + d - v] = 2;
            }
        }
        swap(dp, ndp);
    }

    int best = dp[OFFSET];
    int leftover = total - best;
    cout << leftover << "\n";

    // back‐track
    vector<int> A, B;
    int d = OFFSET;
    for (int i = N - 1; i >= 0; i--) {
        int choice = par[i * (2 * M + 1) + d];
        if (choice == 1) {
            A.push_back(i + 1);
            d -= V[i];
        } else if (choice == 2) {
            B.push_back(i + 1);
            d += V[i];
        }
        // else 0: unassigned → d stays
    }
    // output indices (any order)
    for (int x : A)
        cout << x << " ";
    cout << "\n";
    for (int x : B)
        cout << x << " ";
    cout << "\n";

    return 0;
}