// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int count(string S, char c) {
    if (S.size() == 0) {
        return 0;
    }
    if (S[0] == c) {
        return 1 + count(S.substr(1), c);
    } else {
        return count(S.substr(1), c);
    }
}

// Do not change anything below.
int main() {
    string S;
    char c;
    cin >> S >> c;
    cout << count(S, c) << "\n";
}
