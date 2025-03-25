// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n_of_ships, days, rentals;
    cin >> n_of_ships >> days >> rentals;

    vector<int> ships(days + 1, 0);

    for (int i = 0; i < rentals; i++) {
        int ship_ID, firstday, lastday;
        cin >> ship_ID >> firstday >> lastday;
        for (int j = firstday; j <= lastday; j++) {
            ships[j]++;
        }
    }

    int maxday = 1;
    for (int i = 2; i <= days; i++)
        if (ships[i] > ships[maxday])
            maxday = i;
    cout << maxday << "\n";

    return 0;
}
