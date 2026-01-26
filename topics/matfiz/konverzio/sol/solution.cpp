// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

// Define a function called dec2bin here.
string dec2bin(int n) {
    return n > 0 ? dec2bin(n / 2) + (char)('0' + n % 2) : "";
}

// Do not change anything below.
int main() {
    int a;
    cin >> a;
    cout << dec2bin(a) << '\n';
    return 0;
}
