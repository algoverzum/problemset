#include <bits/stdc++.h>
using namespace std;

// Define a function called anagramma here.

// Do not change anything below.
int main() {
    string a, b;
    cin >> a >> b;
    if (anagramma(a, b))
        cout << 1 << '\n';
    else
        cout << 0 << '\n';
    return 0;
}
