// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;
    cout << S[2] << '\n';
    cout << S[S.size() - 2] << '\n';
    cout << S.substr(0, 5) << '\n';
    cout << S.substr(0, S.size() - 2) << '\n';
    for (size_t i = 1; i < S.size(); i += 2) {
        cout << S[i];
    }
    cout << '\n';
    for (int i = S.size() - 2; i >= 0; i -= 2) {
        cout << S[i];
    }
    cout << '\n';
}
