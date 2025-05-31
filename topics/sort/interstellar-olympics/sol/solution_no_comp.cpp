// @check-accepted: *
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<array<int, 4>> medals(n);
    for (int i = 0; i < n; i++) {
        int g, s, b;
        cin >> g >> s >> b;
        medals[i] = {g, s, b, (i + 1) * (-1)};
    }
    sort(medals.rbegin(), medals.rend());
    for (int i = 0; i < n; i++) {
        cout << medals[i][3] * (-1) << " ";
    }
    cout << "\n";
}
