// @check-accepted: *
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> moons(n);
    for (int i = 0; i < n; i++) {
        cin >> moons[i];
    }
    int sum = 1 + n + accumulate(moons.begin(), moons.end(), 0);
    cout << sum << "\n";
}
