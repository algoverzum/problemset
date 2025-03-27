// @check-accepted: *
#include <iostream>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, num;
    cin >> n >> m;

    set<int> unique_ids;

    for (int i = 0; i < n; i++) {
        cin >> num;
        unique_ids.insert(num);
    }
    for (int i = 0; i < m; i++) {
        cin >> num;
        unique_ids.insert(num);
    }
    cout << unique_ids.size() << "\n";
    for (int id : unique_ids) {
        cout << id << " ";
    }
    cout << "\n";

    return 0;
}