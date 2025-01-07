// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    for (int i = 0; i < word.size(); i++) {
        if (word[i] != word[word.size() - 1 - i]) {
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
}
