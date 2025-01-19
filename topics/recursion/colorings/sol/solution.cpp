// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int n;

void colorings(string S) {
    if (S.size() == n) {
        cout << S << "\n";
        return;
    }
    if (S.length() == 0 || S.back() == 'W') {
        colorings(S + "R");
    }
    colorings(S + "W");
}

int main() {
    cin >> n;
    colorings("");
}
