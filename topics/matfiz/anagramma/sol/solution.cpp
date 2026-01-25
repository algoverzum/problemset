// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

// Define a function called anagramma here.

bool anagramma(string s1, string s2) {
    if (s1.size() != s2.size())
        return false;
    vector<int> db(26);
    for (char c : s1)
        db[c - 'a']++;
    for (char c : s2)
        db[c - 'a']--;
    for (int i = 0; i < 26; i++) {
        if (db[i] != 0)
            return false;
    }
    return true;
}

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
