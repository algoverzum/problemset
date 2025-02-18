// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    vector<int> formation(n);
    sort(v.begin(), v.end(), greater<int>());
    for (int i = 0; i < n; i++) {
        if (i % 2 == 1) {
            formation[n / 2 - (i + 1) / 2] = v[i];
        } else {
            formation[n / 2 + (i + 1) / 2] = v[i];
        }
    }
    for (int s : formation) {
        cout << s << " ";
    }
    cout << "\n";
}
