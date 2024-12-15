// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string uzenet;
    char betu;
    cin >> uzenet >> betu;
    size_t elso = uzenet.find(betu);
    size_t utolso = uzenet.rfind(betu);
    if (elso != string::npos && elso != utolso) {
        string reszlet = uzenet.substr(elso, utolso - elso + 1);
        cout << reszlet << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}