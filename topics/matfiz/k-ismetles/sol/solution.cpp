// @check-accepted: *
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s;
    int k;
    cin >> k >> s;

    vector<int> freq(26, 0);
    for (char c : s) {
        freq[c - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (freq[i] % k != 0) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
