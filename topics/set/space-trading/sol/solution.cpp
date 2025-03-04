// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    set<int> first_ship, second_ship;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        first_ship.insert(num);
    }
    for (int i = 0; i < m; i++) {
        int num;
        cin >> num;
        second_ship.insert(num);
    }
    vector<int> intersection;
    for (int id : first_ship) {
        if (second_ship.count(id) != 0) {
            intersection.push_back(id);
        }
    }
    for (int id : intersection) {
        cout << id << " ";
    }
    cout << "\n";
}
