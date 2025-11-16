// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    string binaris;
    cin >> binaris;
    int decimalis = 0, decjegy;
    for (char c : binaris) {
        decjegy = c - '0';
        decimalis = 2 * decimalis + decjegy;
    }
    cout << decimalis << '\n';
    return 0;
}
