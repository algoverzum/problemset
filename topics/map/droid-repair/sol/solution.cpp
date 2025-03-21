// @check-accepted: *
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> droids(n);
    map<int, int> histogram;

    for (int i = 0; i < n; ++i) {
        cin >> droids[i];

        if (histogram.find(droids[i]) != histogram.end()) {
            cout << histogram[droids[i]] << " " << i << "\n";
            return 0;
        }

        histogram[droids[i]] = i;
    }

    cout << "-1\n";
    return 0;
}
