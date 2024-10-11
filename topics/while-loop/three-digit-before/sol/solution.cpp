// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    int current = -1;
    while (current != 0) {
        cin >> current;
        if (100 <= current && current <= 999) {
            count += 1;
        }
    }
    cout << count << "\n";
    return 0;
}
