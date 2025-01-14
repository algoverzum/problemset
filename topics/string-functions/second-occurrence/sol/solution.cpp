// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    int outindex = -2;
    for (int i = 0; i < word.length(); i++) {
        if (word[i] == 'x' && outindex == -2) {
            outindex++;
        } else if (word[i] == 'x' && outindex == -1) {
            outindex = i;
        }
    }
    cout << outindex << "\n";
}
