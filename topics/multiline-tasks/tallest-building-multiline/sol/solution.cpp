// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int maxi;
    cin >> maxi;
    for (int i = 1; i < n; i++) {
        int height;
        cin >> height;
        if (height > maxi) {
            maxi = height;
        }
    }
    cout << maxi << "\n";
    return 0;
}
