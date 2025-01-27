// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> times(n);
    for (int i = 0; i < n; i++) {
        cin >> times[i];
    }
    sort(times.begin(), times.end());
    if (n % 2 == 0) {
        cout << times[(n / 2) - 1] << "\n";
    } else {
        cout << times[n / 2] << "\n";
    }
}
