// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> s(n + 2, vector<int>(m + 2));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> s[i][j];
        }
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i][j] == s[i - 1][j] || s[i][j] == s[i + 1][j] ||
                s[i][j] == s[i][j - 1] || s[i][j] == s[i][j + 1]) {
                cnt++;
            }
        }
    }
    cout << cnt << "\n";
}
