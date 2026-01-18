// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string mondat, szokoznelkul = "";
    getline(cin, mondat);
    for (int i = 0; i < mondat.size(); i++) {
        if (mondat[i] != ' ')
            szokoznelkul += mondat[i];
    }
    cout << szokoznelkul << "\n";
    return 0;
}
