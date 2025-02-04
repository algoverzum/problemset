// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> spaceships(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> spaceships[i][j];
        }
    }
    int index = -1;
    for (int i = 0; i < n; i++) {
        bool sol = false;
        for (int j = 0; j < n; j++) {
            int better = true;
            for (int k = 0; k < m; k++) {
                better &= spaceships[i][k] > spaceships[j][k];
            }
            if (better) {
                sol = true;
            }
        }
        if (sol && index != -1) {
            index = i + 1;
        }
    }
    cout << index << "\n";
}
