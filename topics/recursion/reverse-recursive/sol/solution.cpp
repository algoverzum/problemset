// @check-accepted: *
#include <iostream>
using namespace std;

void reverse() {
    int x;
    cin >> x;
    if (x != 0) {
        reverse();
    }
    cout << x << "\n";
}

int main() { reverse(); }
