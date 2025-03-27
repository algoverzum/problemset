// @check-accepted: *
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    cin.ignore();
    unordered_map<string, string> city_to_planet;
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        string planet, city;
        iss >> planet;
        while (iss >> city) {
            city_to_planet[city] = planet;
        }
    }
    cin >> m;
    cin.ignore();
    for (int i = 0; i < m; i++) {
        string city;
        cin >> city;
        cout << city_to_planet[city] << "\n";
    }
    return 0;
}