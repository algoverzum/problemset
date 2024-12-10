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
    int i = 0;
    while (i < n - 1 && codes[i] != codes[i + 1])
        i++;
    if (i < n - 1)
        cout << i + 1 << "\n";
    else
        cout << "0\n";
}
