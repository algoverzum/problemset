// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> price(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> price[i][j];
        }
    }
    int k;
    cin >> k;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << k * price[i][j] << " ";
        }
        cout << "\n";
    }
}
