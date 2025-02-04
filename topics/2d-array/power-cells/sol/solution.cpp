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
    int maximal = powercells[0][0];
    int maxindexi = 0;
    int maxindexj = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (powercells[i][j] > maximal) {
                maximal = powercells[i][j];
                maxindexi = i;
                maxindexj = j;
            }
        }
    }
    cout << maxindexi << " " << maxindexj << "\n";
}
