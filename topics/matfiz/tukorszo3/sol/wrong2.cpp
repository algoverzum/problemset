// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string mondat, szn = "", ford = "";
    getline(cin, mondat);
    for (int i = 0; i < mondat.size(); i++) {
        if (mondat[i] != ' ')
            szn += mondat[i];
    }
    for (int i = szn.size() - 1; i >= 0; i--) {
        ford = ford + szn[i];
    }
    if (ford == szn)
        cout << "1\n";
    else
        cout << "0\n";
}
