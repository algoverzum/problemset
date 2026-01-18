// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string mondat, kisbetu = "";
    bool palindrom = true;
    getline(cin, mondat);
    for (char c : mondat) {
        if (isalpha(c))
            kisbetu += tolower(c);
    }
    int hossz = kisbetu.size();
    int i = 0;
    while (i < hossz / 2 and palindrom) {
        if (kisbetu[i] != kisbetu[hossz - 1 - i])
            palindrom = false;
        i++;
    }
    if (palindrom)
        cout << "1\n";
    else
        cout << "0\n";
    return 0;
}
