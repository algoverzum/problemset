// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> oxi_levels(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> oxi_levels[i][j];
        }
    }
    vector<int> nicedays;
    for (int i = 1; i < m; i++) {
        bool valid = true;
        for (int j = 0; j < n; j++) {
            valid &= oxi_levels[j][i] > oxi_levels[j][i - 1];
        }
        if (valid) {
            nicedays.push_back(i + 1);
        }
    }
    cout << nicedays.size() << "\n";
    for (int i : nicedays) {
        cout << i << " ";
    }
    cout << "\n";
}
