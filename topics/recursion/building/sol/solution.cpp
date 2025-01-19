// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

void building(string S, int n) {
    if (S.length() == n) {
        cout << S << "\n";
        return;
    }
    if (S.length() == 0) {
        building(S + "R", n);
        building(S + "W", n);
    } else {
        if (S[S.length() - 1] == 'W') {
            building(S + "R", n);
        }
        building(S + "W", n);
    }
}

int main() {
    int n;
    cin >> n;
    string S = "";
    building(S, n);
}
