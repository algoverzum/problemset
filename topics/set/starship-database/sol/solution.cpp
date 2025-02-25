// @check-accepted: *
#include <iostream>
#include <set>
using namespace std;

int main() {
    int n;
    cin >> n;
    set<int> database;
    for (int i = 0; i < n; i++) {
        int y, x;
        cin >> y >> x;
        if (y == 1)
            database.insert(x);
        if (y == 2)
            database.erase(x);
        if (y == 3) {
            if (database.count(x)) {
                cout << "1" << "\n";
            } else {
                cout << "0" << "\n";
            }
        }
    }
}
