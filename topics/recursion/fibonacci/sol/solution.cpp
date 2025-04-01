// @check-accepted: *
// warning: this is exponential!!!
#include <iostream>
using namespace std;

long long fibonacci(int n) {
    if (n <= 2)
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Do not change anything below.
int main() {
    for (int i = 1; i <= 30; i++) {
        cout << fibonacci(i) << "\n";
    }
}
