// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max = *max_element(a.begin(), a.end());
    int sum = 0;
    for (int x : a) {
        sum += x;
    }

    cout << max * n - sum << '\n';
    return 0;
}
