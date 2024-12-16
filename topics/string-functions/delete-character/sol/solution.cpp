// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    char letter;
    cin >> word >> letter;
    // word.erase(remove(word.begin(), word.end(), letter), word.end());
    for (int i = 0; i < word.length(); i++) {
        if (word[i] != letter) {
            cout << word[i];
        }
    }
    cout << "\n";
    return 0;
}