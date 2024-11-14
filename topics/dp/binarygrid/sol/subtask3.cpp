// @check-accepted: examples NMsmall N1 Nsmall
// @check-time-limit-exceeded: no-limits
/**
 *    author:  BERNARD B.01
**/
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int tt;
  cin >> tt;
  while (tt--) {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    const int inf = int(1e9) + 9;
    int ans = inf;
    for (int mask_i = 0; mask_i < (1 << n); mask_i++) {
      auto Get = [&](int i, int j, int f) {
        return (a[i][j] ^ ((mask_i >> i) & 1) ^ f);
      };
      if (m < 2) {
        bool fail = false;
        for (int i = 2; i < n; i++) {
          if (Get(i, 0, 0) == Get(i - 1, 0, 0) && Get(i, 0, 0) == Get(i - 2, 0, 0)) {
            fail = true;
            break;
          }
        }
        if (!fail) {
          ans = min(ans, __builtin_popcount(mask_i));
        }
        continue;
      }
      array<array<int, 2>, 2> dp;
      for (int f1 : {0, 1}) {
        bool fail = false;
        for (int i = 2; i < n; i++) {
          if (Get(i, 0, f1) == Get(i - 1, 0, f1) && Get(i, 0, f1) == Get(i - 2, 0, f1)) {
            fail = true;
            break;
          }
        }
        if (fail) {
          for (int f2 : {0, 1}) {
            dp[f1][f2] = inf;
          }
          continue;
        }
        for (int f2 : {0, 1}) {
          fail = false;
          for (int i = 2; i < n; i++) {
            if (Get(i, 1, f2) == Get(i - 1, 1, f2) && Get(i, 1, f2) == Get(i - 2, 1, f2)) {
              fail = true;
              break;
            }
          }
          dp[f1][f2] = (fail ? inf : f1 + f2);
        }
      }
      for (int j = 2; j < m; j++) {
        array<array<int, 2>, 2> new_dp;
        for (int f1 : {0, 1}) {
          for (int f2 : {0, 1}) {
            new_dp[f1][f2] = inf;
          }
        }
        for (int f1 : {0, 1}) {
          for (int f2 : {0, 1}) {
            for (int f3 : {0, 1}) {
              bool fail = false;
              for (int i = 0; i < n; i++) {
                if (Get(i, j, f3) == Get(i, j - 1, f2) && Get(i, j, f3) == Get(i, j - 2, f1)) {
                  fail = true;
                  break;
                }
                if (i > 1 && Get(i, j, f3) == Get(i - 1, j, f3) && Get(i, j, f3) == Get(i - 2, j, f3)) {
                  fail = true;
                  break;
                }
              }
              if (!fail) {
                new_dp[f2][f3] = min(new_dp[f2][f3], f3 + dp[f1][f2]);
              }
            }
          }
        }
        swap(dp, new_dp);
      }
      for (int f1 : {0, 1}) {
        for (int f2 : {0, 1}) {
          ans = min(ans, dp[f1][f2] + __builtin_popcount(mask_i));
        }
      }
    }
    cout << (ans >= inf ? -1 : ans) << '\n';
  }
  return 0;
}
