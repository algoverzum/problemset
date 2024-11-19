// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;
    int n = S.size();
    cout << S[0] << S[n - 1] << '\n';
    for (int i = n - 1; i >= 0; i--) {
        cout << S[i];
    }
    cout << '\n';
    for (int i = 2; i < n; i += 3) {
        cout << S[i];
    }
    cout << '\n';
    cout << S.substr(0, n / 2) << '\n';
    cout << S.substr(n / 2) << '\n';
}
