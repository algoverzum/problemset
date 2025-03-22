// @check-accepted: examples
// @check-time-limit-exceeded: all
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> droids;

    for (int i = 0; i < n; ++i) {
        int num;
        cin >> num;

        for (int j = 0; j < droids.size(); ++j) {
            if (droids[j] == num) {
                cout << j << " " << i << endl;
                return 0;
            }
        }

        droids.push_back(num);
    }

    cout << -1 << endl;
    return 0;
}
