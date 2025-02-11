// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> powercells(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> powercells[i][j];
        }
    }
    int maxi = 0, maxj = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (powercells[i][j] > powercells[maxi][maxj]) {
                maxi = i;
                maxj = j;
            }
        }
    }
    cout << maxi + 1 << " " << maxj + 1 << "\n";
}
