// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> flights(n);
    for (int i = 0; i < n; i++) {
        cin >> flights[i];
    }
    for (int i = 0; i < n; i += 2)
        cout << flights[i] << ' ';
    cout << "\n";
    for (int i = 1; i < n; i += 2)
        cout << flights[i] << ' ';
    cout << "\n";
}
