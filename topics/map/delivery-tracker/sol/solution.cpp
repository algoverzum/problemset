// @check-accepted: *
#include <iostream>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;

    map<pair<int, int>, long long> deliveries;

    for (int i = 0; i < n; ++i) {
        int x, y;
        long long p;
        cin >> x >> y >> p;
        deliveries[{x, y}] += p;
    }

    long long max_packages = 0;
    pair<int, int> best_location;

    for (const auto &entry : deliveries) {
        if (entry.second > max_packages) {
            max_packages = entry.second;
            best_location = entry.first;
        }
    }

    cout << best_location.first << " " << best_location.second << " "
         << max_packages << endl;

    return 0;
}
