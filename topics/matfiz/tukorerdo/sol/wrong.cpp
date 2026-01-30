// @check-wrong-answer: *
#include <iostream>
using namespace std;

int main() {
    string word1, word2;
    cin >> word1, word2;
    if (word1[0] == word2.back()) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
