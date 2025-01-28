// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> names(n);
    for (int i = 0; i < n; i++) {
        cin >> names[i];
    }
    sort(names.begin(), names.end());
    for (int i = 0; i < n; i++) {
        cout << names[i] << " ";
    }
    cout << "\n";
}
