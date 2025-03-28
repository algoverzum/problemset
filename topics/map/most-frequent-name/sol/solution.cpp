// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    map<string, int> histogram;

    for (int i = 0; i < n; i++) {
        string ID;
        cin >> ID;
        histogram[ID]++;
    }

    int maxi = 0;
    for (const auto &pair : histogram) {
        if (pair.second > maxi) {
            maxi = pair.second;
        }
    }

    vector<string> most_frequent;
    for (const auto &pair : histogram) {
        if (pair.second == maxi) {
            most_frequent.push_back(pair.first);
        }
    }

    sort(most_frequent.begin(), most_frequent.end());
    cout << maxi << "\n";
    for (string ship : most_frequent) {
        cout << ship << "\n";
    }

    return 0;
}
