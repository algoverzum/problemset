// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> tactics(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> tactics[i][j];
        }
    }
    int c;
    cin >> c;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << c * tactics[i][j] << " ";
        }
        cout << "\n";
    }
}
