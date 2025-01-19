// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> db(n);
    vector<string> q(m);
    vector<string> database(n);
    for (int i = 0; i < n; i++) {
        cin >> database[i];
    }

    vector<string> queries(m);
    for (int i = 0; i < m; i++) {
        cin >> queries[i];
    }
    vector<int> result;
    for (string query : queries) {
        auto it = find(database.begin(), database.end(), query);
        if (it != database.end()) {
            result.push_back(distance(database.begin(), it) + 1);
        } else {
            result.push_back(-1);
        }
    }
    for (size_t i = 0; i < m; i++) {
        cout << result[i] << " ";
    }
    cout << "\n";
}
