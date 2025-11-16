// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    string bin = "";
    int dec;
    cin >> dec;
    if (dec == 0) {
        cout << 0 << "\n";
        return 0;
    }
    while (dec != 0) {
        int maradek = dec % 2;
        bin = bin + char(maradek + '0');
        dec /= 2;
    }
    for (int i = bin.size() - 1; i >= 0; i--)
        cout << bin[i];
    cout << "\n";
    return 0;
}
