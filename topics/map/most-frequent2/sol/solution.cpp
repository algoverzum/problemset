// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    map<int, int> histogram;

    for (int i = 0; i < n; i++) {
        int ID;
        cin >> ID;
        histogram[ID]++;
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
