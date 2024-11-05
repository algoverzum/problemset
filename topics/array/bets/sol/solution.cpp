
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> money(n);
    for (int i = 0; i < n; ++i) {
        cin >> money[i];
    }
    vector<int> win(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        win[i] = money[i + 1] - money[i];
    }
    vector<int> diff(n - 2);
    for (int i = 0; i < n - 2; ++i) {
        diff[i] = win[i + 1] - win[i];
    }
    for (int i = 0; i < n - 1; ++i) {
        cout << win[i] << " ";
    }
    cout << "\n";
    for (int i = 0; i < n - 2; ++i) {
        cout << diff[i] << " ";
    }
    cout << "\n";
    return 0;
}
