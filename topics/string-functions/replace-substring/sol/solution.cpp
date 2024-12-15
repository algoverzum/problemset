// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int i = 0; i <= S.size() - 4; i++) {
        if (S.substr(i, 4) == "FEAR") {
            S[i] = 'H';
            S[i + 1] = 'O';
            S[i + 2] = 'P';
            S[i + 3] = 'E';
        }
    }
    cout << S << "\n";
}
