// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;
int main() {
    string word;
    char key;
    cin >> word >> key;
    int i = 0;
    while (word[i] != key) {
        if (i == word.length() - 1) {
            cout << -1 << "\n";
            return 0;
        }
        i++;
    }
    cout << i + 1 << "\n";
    return 0;
}
