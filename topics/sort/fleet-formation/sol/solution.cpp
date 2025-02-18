// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> ships(n);
    for (int i = 0; i < n; i++) {
        cin >> ships[i];
    }
    vector<int> formation(n);
    sort(ships.begin(), ships.end(), greater<int>());
    for (int i = 0; i < n; i++) {
        if (i % 2 == 1) {
            formation[n / 2 - (i + 1) / 2] = ships[i];
        } else {
            formation[n / 2 + (i + 1) / 2] = ships[i];
        }
    }
    for (int s : formation) {
        cout << s << " ";
    }
    cout << "\n";
}
