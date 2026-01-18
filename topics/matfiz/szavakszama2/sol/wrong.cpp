// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string mondat;
    int db = 1;
    getline(cin, mondat);
    for (int i = 0; i < mondat.size(); i++) {
        if (mondat[i] == ' ')
            db++;
    }
    cout << db << "\n";
    return 0;
}
