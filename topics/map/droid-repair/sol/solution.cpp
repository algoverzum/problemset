// @check-accepted: *
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    map<int, int> index;

    for (int i = 1; i <= n; ++i) {
        int droid;
        cin >> droid;

        if (index.count(droid)) {
            cout << index[droid] << " " << i << "\n";
            return 0;
        }

        index[droid] = i;
    }

    cout << "-1\n";
    return 0;
}
