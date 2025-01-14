// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;
    char letter;
    cin >> message >> letter;
    size_t first = message.find(letter);
    size_t last = message.rfind(letter);
    if (first != string::npos) {
        cout << message.substr(first, last - first + 1) << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}