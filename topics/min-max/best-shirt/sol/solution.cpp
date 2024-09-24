// @check-accepted: *
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> prices(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> prices[i];
    }

    int maxindex = 0;
    int maxvalue = 0;
    for (int i = 1; i <= n; i++) {
        if (prices[i] <= k && prices[i] > maxvalue) {
            maxindex = i;
            maxvalue = prices[i];
        }
    }
    cout << maxindex << "\n" << maxvalue << "\n";
    return 0;
}
