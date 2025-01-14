// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word;
    int beauty = 0;
    for (int i = 0; i < word.length() - 2; i++) {
        if (word.substr(i, 3) == "obo") {
            beauty++;
        }
    }
    cout << beauty << "\n";
}
