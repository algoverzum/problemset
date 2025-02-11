// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> A(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> A[i][j];
        }
    }
    int i, j;
    cin >> i >> j;
    i--;
    j--;

    for (int k = 0; k < n; k++) {
        swap(A[k][i], A[k][j]);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << A[i][j] << " ";
        }
        cout << "\n";
    }
}
