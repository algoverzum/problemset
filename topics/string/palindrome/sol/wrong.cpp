// @check-wrong-answer: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    if (word[0] == word.back()) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
