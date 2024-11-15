// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word1, word2;
    cin >> word1 >> word2;
    if (word2.size() > word1.size()) {
        cout << word2 << "\n";
    } else {
        cout << word1 << "\n";
    }
}
