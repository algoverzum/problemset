// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> allomasok(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> allomasok[i][j];
        }
    }
    vector<int> highdays;
    for (int i = 1; i < m; i++) {
        bool megfelel = true;
        for (int j = 0; j < n; j++) {
            megfelel &= allomasok[j][i] > allomasok[j][i - 1];
        }
        if (megfelel) {
            highdays.push_back(i + 1);
        }
    }
    cout << highdays.size() << "\n";
    for (int i : highdays) {
        cout << i << " ";
    }
    cout << "\n"
}
