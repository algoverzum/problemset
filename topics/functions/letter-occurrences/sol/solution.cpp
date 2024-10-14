// @check-accepted: *
#include <iostream>
using namespace std;

int count(string word, char letter) {
    int cnt = 0;
    for (char c : word) {
        if (c == letter)
            cnt++;
    }
    return cnt;
}

int main() {
    cout << count("chocolate", 'c') << "\n";
    cout << count("chocolate", 'b') << "\n";
    cout << count("tree", 't') << "\n";
    cout << count("tree", 'e') << "\n";
    cout << count("", 'x') << "\n";
    cout << count("oooooooooo", 'o') << "\n";
    cout << count("shshshshshshshsh", 's') << "\n";
    cout << count("pneumonoultramicroscopicsilicovolcanoconiosis", 'i') << "\n";
}
