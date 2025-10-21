// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string tipp1, tipp2;
    cin >> tipp1 >> tipp2;
    if (tipp1 == tipp2) {
        cout << "0\n";
    } else if (tipp1 == "ko" && tipp2 == "ollo" ||
               tipp1 == "ollo" && tipp2 == "papir" ||
               tipp1 == "papir" && tipp2 == "ko") {
        cout << "1\n";
    } else {
        cout << "2\n";
    }
}
