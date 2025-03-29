// @check-accepted: *
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    map<string, string> city_to_planet;
    for (int i = 0; i < n; i++) {
        int cities;
        string planet, city;
        cin >> planet;
        cin >> cities;
        for (int j = 0; j < cities; j++) {
            cin >> city;
            city_to_planet[city] = planet;
        }
    }
    cin >> m;
    for (int i = 0; i < m; i++) {
        string city;
        cin >> city;
        cout << city_to_planet[city] << "\n";
    }
    return 0;
}
