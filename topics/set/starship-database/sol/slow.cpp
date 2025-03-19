// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> database;
    for (int i = 0; i < n; i++) {
        int t, x;
        cin >> t >> x;
        if (t == 1 && !count(database.begin(), database.end(), x))
            database.push_back(x);
        if (t == 2) {
            auto it = find(database.begin(), database.end(), x);
            if (it != database.end())
                database.erase(it);
        }
        if (t == 3) {
            cout << count(database.begin(), database.end(), x) << "\n";
        }
    }
}
