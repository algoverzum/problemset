// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, count = 0;
    cin >> n;
    string word;
    for (int i = 0; i < n; i++) {
        cin >> word;
        if (word.find('o') < word.length()) {
            count++;
        }
    }
    cout << count << "\n";
}
