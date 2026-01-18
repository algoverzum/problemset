// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string s;
    int n, szum = 0;
    cin >> s;
    for (int i = 0; i < s.size(); i++)
        szum += s[i] - '0';
    while (szum > 9) {
        n = szum;
        szum = 0;
        do {
            szum += n % 10;
            n = n / 10;
        } while (n != 0);
    }
    if (szum == 1)
        cout << "1\n";
    else
        cout << "0\n";
    return 0;
}
