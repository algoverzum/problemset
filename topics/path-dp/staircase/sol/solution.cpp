// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> res(n + 1, 0);
    res[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = max(0, i - k); j < i; j++) {
            res[i] += res[j];
        }
    }

    cout << res[n] << "\n";
}
