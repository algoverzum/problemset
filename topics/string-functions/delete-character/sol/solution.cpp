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
    replace(word.begin(), word.end(), letter, ' ');
    word.erase(remove(word.begin(), word.end(), ' '), word.end());
    cout << word << "\n";
    return 0;
}