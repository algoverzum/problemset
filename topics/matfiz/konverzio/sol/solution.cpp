// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

// Define a function called dec2bin here.
string dec2bin(int n) {
    string bin = "";
    while (n > 0) {
        int maradek = n % 2;
        bin = char(maradek + '0') + bin;
        n /= 2;
    }
    return bin;
}

// Do not change anything below.
int main() {
    int a;
    cin >> a;
    cout << dec2bin(a) << '\n';
    return 0;
}
