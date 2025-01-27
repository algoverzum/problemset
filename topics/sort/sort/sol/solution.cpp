// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> elements(n);
    for (int i = 0; i < n; i++) {
        cin >> elements[i];
    }
    sort(elements.begin(), elements.end());
    for (int i = 0; i < n; i++) {
        cout << elements[i] << " ";
    }
    cout << "\n";
    sort(elements.begin(), elements.end(), greater<int>());
    for (int i = 0; i < n; i++) {
        cout << elements[i] << " ";
    }
    cout << "\n";
}
