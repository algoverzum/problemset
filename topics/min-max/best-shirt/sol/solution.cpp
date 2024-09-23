// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int k;
    cin >> k;
    int maximal = 0;
    int maxindex;
    for (int i = 0; i < n; i++) {
        int current;
        cin >> current;
        if (current <= k && current > maximal) {
            maximal = current;
            maxindex = i + 1;
        }
    }
    cout << maxindex << "\n" << maximal << "\n";
    return 0;
}
