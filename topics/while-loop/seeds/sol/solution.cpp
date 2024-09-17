// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int seeds = 1;
    while (seeds < n) {
        seeds *= 3;
    }
    cout << seeds << "\n";
    return 0;
}
