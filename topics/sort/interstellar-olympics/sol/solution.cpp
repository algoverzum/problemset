// @check-accepted: *
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>
using namespace std;

bool Compare(array<int, 4> a, array<int, 4> b) {
    if (get<0>(a) != get<0>(b)) {
        return a[0] > b[0];
    } else if (a[1] != b[1]) {
        return a[1] > b[1];
    } else if (a[2] != b[2]) {
        return a[2] > b[2];
    } else {
        return a[3] < b[3];
    }
}

int main() {
    int n;
    cin >> n;
    vector<array<int, 4>> medals(n);
    for (int i = 0; i < n; i++) {
        int g, s, b;
        cin >> g >> s >> b;
        medals[i] = {g, s, b, i + 1};
    }
    sort(medals.begin(), medals.end(), Compare);
    for (int i = 0; i < n; i++) {
        cout << medals[i][3] << " ";
    }
    cout << "\n";
}
