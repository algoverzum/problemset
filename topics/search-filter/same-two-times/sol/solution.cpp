// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> codes(n);
    for (int i = 0; i < n; i++) {
        cin >> codes[i];
    }
    int index = -1;
    for (int i = 0; i < n - 1; i++) {
        if (codes[i] == codes[i + 1]) {
            index = i;
        }
    }
    cout << index + 1 << "\n";
}
