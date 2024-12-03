// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> days(n);
    for (int i = 0; i < n; i++) {
        cin >> days[i];
    }
    int i = 0;
    while (i < n && days[i] != 0)
        i++;
    if (i < n) {
        cout << i + 1 << "\n";
    } else {
        cout << -1 << "\n";
    }
}
