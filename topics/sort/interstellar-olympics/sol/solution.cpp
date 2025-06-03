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
        int gold, silver, bronze;
        cin >> gold >> silver >> bronze;
        medals[i] = {-gold, -silver, -bronze, i + 1};
    }
    sort(medals.begin(), medals.end());
    for (auto m : medals) {
        cout << m[3] << " ";
    }
    cout << "\n";
}
