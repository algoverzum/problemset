// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    int first = word.find('x');
    if (first == -1) {
        cout << -2 << "\n";
        return 0;
    }
    int second = word.find('x', first + 1);
    cout << second << "\n";
}
