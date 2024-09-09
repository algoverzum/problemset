// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
<<<<<<< HEAD
    int n;
    cin >> n;
    cout << 42 << "\n";
    return 0;
=======
    int n;
    cin >> n;
    int divisors = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            divisors++;
        }
    }
    cout << divisors << "\n";
>>>>>>> 300991843902251dbdcceaeb00fc0f23adfaa6f0
}
