// @check-accepted: examples NMsmall
// @check-time-limit-exceeded: Nsmall
// @check-zero: N1 no-limits
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
    int ans = INT_MAX;
    for (int mask_i = 0; mask_i < (1 << n); mask_i++) {
      for (int mask_j = 0; mask_j < (1 << m); mask_j++) {
        auto Get = [&](int i, int j) {
          return (a[i][j] ^ ((mask_i >> i) & 1) ^ ((mask_j >> j) & 1));
        };
        bool fail = false;
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < m - 2; j++) {
            if (Get(i, j) == Get(i, j + 1) && Get(i, j) == Get(i, j + 2)) {
              fail = true;
              break;
            }
          }
          if (fail) {
            break;
          }
        }
        if (fail) {
          continue;
        }
        for (int j = 0; j < m; j++) {
          for (int i = 0; i < n - 2; i++) {
            if (Get(i, j) == Get(i + 1, j) && Get(i, j) == Get(i + 2, j)) {
              fail = true;
              break;
            }
          }
          if (fail) {
            break;
          }
        }
        if (!fail) {
          ans = min(ans, __builtin_popcount(mask_i) + __builtin_popcount(mask_j));
        }
      }
    }
    if (ans == INT_MAX) {
      cout << -1 << '\n';
    } else {
      cout << ans << '\n';
    }
  }
  return 0;
}
