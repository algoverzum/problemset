// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;

    map<int, int> histogram;

    for (int i = 0; i < n; i++) {
        int id;
        cin >> id;
        histogram[id]++;
    }

    int maxi = 0;
    for (auto [id, cnt] : histogram) {
        maxi = max(maxi, cnt);
    }

    vector<int> most_frequent;
    for (auto [id, cnt] : histogram) {
        if (cnt == maxi) {
            cout << id << " ";
        }
    }
    cout << "\n";

    return 0;
}
