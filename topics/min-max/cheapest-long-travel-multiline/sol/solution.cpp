// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int cheapest = -1;
    for (int i = 0; i < n; i++) {
        int distance, price;
        cin >> distance >> price;
        if (distance >= k) {
            if (cheapest == -1 || cheapest > price) {
                cheapest = price;
            }
        }
    }
    cout << cheapest << "\n";
    return 0;
}
