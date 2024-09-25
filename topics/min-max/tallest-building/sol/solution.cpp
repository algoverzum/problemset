// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    int maxi = h[0];
    for (int i = 1; i < n; i++) {
        if (h[i] > maxi) {
            maxi = h[i];
        }
    }
    cout << maxi << "\n";
    return 0;
}
