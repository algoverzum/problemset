// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string tipp1, tipp2;
    cin >> tipp1 >> tipp2;
    if (tipp1 == tipp2)
        cout << 0 << "\n";
    if (tipp1 == "ko" and tipp2 == "ollo" or
        tipp1 == "ollo" and tipp2 == "papir" or
        tipp1 == "papir" and tipp2 == "ko")
        cout << 1 << "\n";
    if (tipp1 == "ko" and tipp2 == "papir" or
        tipp1 == "papir" and tipp2 == "ollo" or
        tipp1 == "ollo" and tipp2 == "ko")
        cout << 2 << "\n";
}
