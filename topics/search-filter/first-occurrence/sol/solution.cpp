// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;
int main() {
    string word;
    char key;
    cin >> word >> key;
    int i = 0;
    while (i < word.size() && word[i] != key) {
        i++;
    }
    if (i < word.size())
        cout << i + 1 << "\n";
    else
        cout << "-1\n";
    return 0;
}
