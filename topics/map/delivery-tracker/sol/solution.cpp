// @check-accepted: *
#include <iostream>
#include <map>
using namespace std;

using ll = long long;

int main() {
    int n;
    cin >> n;

    map<pair<int, int>, ll> deliveries;

    for (int i = 0; i < n; ++i) {
        int x, y;
        ll p;
        cin >> x >> y >> p;
        deliveries[{x, y}] += p;
    }

    ll max_packages = 0;
    pair<int, int> best_location;

    for (auto [location, packages] : deliveries) {
        if (packages > max_packages) {
            max_packages = packages;
            best_location = location;
        }
    }

    cout << best_location.first << " " << best_location.second << " "
         << max_packages << "\n";

    return 0;
}
