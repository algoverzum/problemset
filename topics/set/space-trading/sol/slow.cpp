// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> first_ship(n), second_ship(m);
    for (int i = 0; i < n; i++) {
        cin >> first_ship[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> second_ship[i];
    }
    if (n < m)
        swap(first_ship, second_ship);
    vector<int> intersection;
    for (int id : first_ship) {
        if (find(second_ship.begin(), second_ship.end(), id) !=
            second_ship.end()) {
            intersection.push_back(id);
        }
    }
    sort(intersection.begin(), intersection.end());
    cout << intersection.size() << "\n";
    for (int id : intersection) {
        cout << id << " ";
    }
    cout << "\n";
}
