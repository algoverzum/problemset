// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int n;

void building(string S) {
    if (S.size() == n) {
        cout << S << "\n";
        return;
    }
    if (S.length() == 0 || S.back() == 'W') {
        building(S + "R");
    }
    building(S + "W");
}

int main() {
    cin >> n;
    building("");
}
