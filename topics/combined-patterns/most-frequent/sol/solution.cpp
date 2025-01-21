// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int mostFrequent = a[0], maxCount = 1;
    for (int i = 0; i < n; i++) {
        int cnt = count(a.begin(), a.end(), a[i]);
        if (cnt > maxCount) {
            mostFrequent = a[i];
            maxCount = cnt;
        } else if (cnt == maxCount) {
            if (mostFrequent > a[i]) {
                mostFrequent = a[i];
            }
        }
    }

    cout << mostFrequent << "\n";
}
