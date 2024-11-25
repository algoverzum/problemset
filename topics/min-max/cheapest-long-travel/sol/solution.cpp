// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> distance(n);
    for (int i = 0; i < n; i++) {
        cin >> distance[i];
    }
    vector<int> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    int cheapest = -1;
    for (int i = 0; i < n; i++) {
        if (distance[i] >= k) {
            if (cheapest == -1 || cheapest > price[i]) {
                cheapest = price[i];
            }
        }
    }
    cout << cheapest << "\n";
    return 0;
}
