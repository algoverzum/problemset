// @check-accepted: *
#include <algorithm>
#include <functional>
#include <iostream>
#include <math.h>
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
        // formation[((n)/2)+int((pow(-1,i)*(i+1)/2))]=v[i];
        if (i % 2 == 1) {
            formation[n / 2 - (i + 1) / 2] = v[i];
        } else {
            formation[n / 2 + (i + 1) / 2] = v[i];
        }
    }
    for (int i = 0; i < n; i++) {
        cout << formation[i] << " ";
    }
    cout << "\n";
}
