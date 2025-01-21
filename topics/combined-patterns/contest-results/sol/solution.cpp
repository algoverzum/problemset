// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<string> result(n);
    for (int i = 0; i < n; i++) {
        cin >> result[i];
    }

    for (int i = 0; i < q; i++) {
        string query;
        cin >> query;
        auto it = find(result.begin(), result.end(), query);
        if (it != result.end()) {
            cout << it - result.begin() + 1 << " ";
        } else {
            cout << "-1 ";
        }
    }
    cout << "\n";
}
