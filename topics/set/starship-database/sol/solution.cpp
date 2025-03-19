// @check-accepted: *
#include <iostream>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    set<int> database;
    for (int i = 0; i < n; i++) {
        int t, x;
        cin >> t >> x;
        if (t == 1)
            database.insert(x);
        else if (t == 2)
            database.erase(x);
        else
            cout << database.count(x) << "\n";
    }
}
