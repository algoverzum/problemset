// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word;
    int beauty = 0;
    for (int i = 0; i + 2 < word.length(); i++) {
        if (word.substr(i, 3) == "ebo") {
            beauty++;
        }
    }
    cout << beauty << "\n";
}
