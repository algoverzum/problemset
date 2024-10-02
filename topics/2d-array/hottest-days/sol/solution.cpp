// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> t(n, vector<int>(m));
    int maxi = -50;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> t[i][j];
            maxi = max(maxi, t[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        for (int j = 0; j < m; j++) {
            if (t[i][j] == maxi) cnt++;
        }
        cout << cnt << "\n";
    }
}
