// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<array<int, 3>> teams(n);
    for (int i = 1; i <= n; i++) {
        int a, b;
        cin >> a >> b;
        teams.push_back({-a, b, i});
    }
    sort(teams.begin(), teams.end());
    for (auto [a, b, index] : teams) {
        cout << index << " ";
    }
    cout << "\n";
    return 0;
}
