// @check-accepted: *
#include <iostream>
using namespace std;

bool contains(string word, char letter) {
    for (char c : word) {
        if (c == letter)
            return true;
    }
    return false;
}

string common_letters(string s, string t) {
    string common;
    for (char c = 'a'; c <= 'z'; c++) {
        if (contains(s, c) && contains(t, c)) {
            common += c;
        }
    }
    return common;
}

int main() {
    cout << common_letters("apple", "leaves") << "\n";
    cout << common_letters("chocolate", "catching") << "\n";
    cout << common_letters("chocolate", "chocolate") << "\n";
    cout << common_letters("chocolate", "banana") << "\n";
    cout << common_letters("chocolate", "drums") << "\n";
    cout << common_letters("tree", "e") << "\n";
    cout << common_letters("", "x") << "\n";
    cout << common_letters("oooooooooo", "ooo") << "\n";
    cout << common_letters("shshshshshshshsh", "shake") << "\n";
    cout << common_letters("pneumonoultramicroscopicsilicovolcanoconiosis",
                           "methylenedioxymethamphetamine")
         << "\n";
}
