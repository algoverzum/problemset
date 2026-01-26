// @check-accepted: *
#include <algorithm>
#include <iostream>
using namespace std;

// Define a function called anagramma here.

bool anagramma(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
}

// Do not change anything below.
int main() {
    string a, b;
    cin >> a >> b;
    if (anagramma(a, b))
        cout << "1\n";
    else
        cout << "0\n";
    return 0;
}
