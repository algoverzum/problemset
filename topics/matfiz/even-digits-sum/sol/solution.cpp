// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, szum = 0, jegy;
    cin >> n;
    while (n != 0) {
        jegy = n % 10;
        if (n % 2 == 0)
            szum = szum + jegy;
        n = n / 10;
    }
    cout << szum << "\n";
    return 0;
}
