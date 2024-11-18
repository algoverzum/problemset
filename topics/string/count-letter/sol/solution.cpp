// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    int letterCount = 0;
    for (int i = 0; i < word.size(); i++) {
        if (word[i] == 'p') {
            letterCount++;
        }
    }
    cout << letterCount << "\n";
}
