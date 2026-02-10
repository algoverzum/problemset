// @check-accepted: *
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<array<int, 3>> teams(n);
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        teams[i] = {-a, b, i + 1};
    }
    sort(teams.begin(), teams.end());
    for (auto [a, b, index] : teams) {
        cout << index << " ";
    }
    cout << "\n";
    return 0;
}
