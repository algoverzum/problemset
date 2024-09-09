// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int squarecounter = 1;
    while (squarecounter * squarecounter < n) {
        cout << squarecounter * squarecounter << "\n";
        squarecounter++;
    }
    return 0;
}
