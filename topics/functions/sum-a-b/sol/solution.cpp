// @check-accepted: *
#include <iostream>
using namespace std;

int sum_between(int a, int b) {
    int sum = 0;
    for (int i = a; i <= b; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    cout << sum_between(3, 5) << "\n";
    cout << sum_between(0, 10) << "\n";
    cout << sum_between(42, 42) << "\n";
    cout << sum_between(-1, 1) << "\n";
    cout << sum_between(-5, 3) << "\n";
    cout << sum_between(100, 1000) << "\n";
    cout << sum_between(3141, 5926) << "\n";
    cout << sum_between(1, 10000) << "\n";
}
