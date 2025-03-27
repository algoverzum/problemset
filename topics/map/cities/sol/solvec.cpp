#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<string, string>> city_to_planet;

    for (int i = 0; i < n; ++i) {
        string planet;
        cin >> planet;
        string city;
        while (cin.peek() != '\n' && cin >> city) {
            city_to_planet.emplace_back(city, planet);
        }
    }

    sort(city_to_planet.begin(), city_to_planet.end());

    int m;
    cin >> m;

    for (int i = 0; i < m; ++i) {
        string city;
        cin >> city;

        if (city_to_planet.back().first == city) {
            cout << city_to_planet.back().second << "\n";
        } else {
            int lo = 0, hi = city_to_planet.size() - 1;
            while (hi - lo > 1) {
                int mid = (hi + lo) / 2;
                if (city_to_planet[mid].first > city) {
                    hi = mid;
                } else {
                    lo = mid;
                }
            }
            cout << city_to_planet[lo].second << "\n";
        }
    }

    return 0;
}
