// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string mondat;
    int db = 0, hossz;
    getline(cin, mondat);
    hossz = mondat.size();
    for (int i = 0; i < hossz - 1; i++) {
        if (mondat[i] == ' ' and mondat[i + 1] != ' ')
            db++;
    }
    if (mondat[0] != ' ')
        db++;
    cout << db << '\n';
    return 0;
}
