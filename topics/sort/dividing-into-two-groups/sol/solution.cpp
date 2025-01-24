// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> T(n);
    for (int i = 0; i < n; i++) {
        cin >> T[i];
    }
    sort(T.begin(), T.end());
    int maxi = T[1] - T[0];
    for (int i = 2; i < n; i++) {
        maxi = max(maxi, T[i] - T[i - 1]);
    }
    cout << maxi << "\n";
}
