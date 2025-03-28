// @check-accepted: *

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<int, int> histogram;

    for (int i = 0; i < n; i++) {
        int shipID;
        cin >> shipID;
        histogram[shipID]++;
    }

    int maxi = 0;
    for (const auto &pair : histogram) {
        if (pair.second > maxi) {
            maxi = pair.second;
        }
    }

    vector<int> most_frequent;
    for (const auto &pair : histogram) {
        if (pair.second == maxi) {
            most_frequent.push_back(pair.first);
        }
    }

    sort(most_frequent.begin(), most_frequent.end());

    for (int ship : most_frequent) {
        cout << ship << " ";
    }
    cout << "\n";

    return 0;
}
