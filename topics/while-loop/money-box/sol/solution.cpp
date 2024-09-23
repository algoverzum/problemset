// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int k = 0;
    int day = 0;
    while (k < n) {
        day += 1;
        k += day;
    }
    cout << day << "\n";
    return 0;
}
