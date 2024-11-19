// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    bool pal = true;
    for (int i = 0; i < word.size(); i++) {
        pal &= word[i] == word[word.size() - 1 - i];
    }
    if (pal) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
