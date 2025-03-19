// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int no_of_ships, days, rentals;
    cin >> no_of_ships >> days >> rentals;

    vector<int> ships(days + 1, 0);

    for (int i = 0; i < rentals; i++) {
        int ship_ID, firstday, lastday;
        cin >> ship_ID >> firstday >> lastday;
        for (int j = firstday; j <= lastday; j++) {
            ships[j]++;
        }
    }

    cout << distance(ships.begin(), max_element(ships.begin(), ships.end()))
         << endl;

    return 0;
}
