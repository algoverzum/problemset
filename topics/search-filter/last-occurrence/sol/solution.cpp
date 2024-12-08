// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    char key;
    cin >> word >> key;
    int index = -1;
    for (int i = word.length() - 1; i >= 0; i--) {
        if (word[i] == key) {
            index = i + 1;
            break;
        }
    }
    cout << index << "\n";
    return 0;
}
