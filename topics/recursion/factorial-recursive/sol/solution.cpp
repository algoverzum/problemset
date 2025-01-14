// @check-accepted: *
#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

// Do not change anything below
int main() {
    for (int i = 1; i <= 15; i++) {
        cout << factorial(i) << "\n";
    }
}
