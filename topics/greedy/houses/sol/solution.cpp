// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, B;
        cin >> N >> B;

        vector<int> prices(N);
        for (int i = 0; i < N; i++) {
            cin >> prices[i];
        }

        sort(prices.begin(), prices.end());

        int count = 0;
        long long total = 0;

        for (int price : prices) {
            if (total + price <= B) {
                total += price;
                count++;
            } else {
                break;
            }
        }

        cout << count << "\n";
    }

    return 0;
}
