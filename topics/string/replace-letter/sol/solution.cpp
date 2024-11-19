// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    for (int i = 0; i < word.size(); i++) {
        if (word[i] == 'a') {
            word[i] = 'e';
        }
    }
    cout << word << "\n";
}
