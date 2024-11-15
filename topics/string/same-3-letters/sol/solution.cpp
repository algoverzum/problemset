// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    if (word[0] == word[1] && word[1] == word[2]) {
        cout << "NO" << "\n";
    } else {
        cout << "YES" << "\n";
    }
}
