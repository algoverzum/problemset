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
    int index = -1;
    for (int i = 0; i < n; i++) {
        if (days[i] == 0) {
            index = i + 1;
        }
    }
    cout << index << "\n";
}
