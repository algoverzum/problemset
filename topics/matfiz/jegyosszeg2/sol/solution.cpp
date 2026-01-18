// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int i, szamjegy, szum = 0;
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        szamjegy = s[i] - '0';
        szum += szamjegy;
    }
    cout << szum << '\n';
    return 0;
}
