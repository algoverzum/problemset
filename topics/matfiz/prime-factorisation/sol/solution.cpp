// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, i = 2;
    cin >> n;
    while (n != 1) {
        while (n % i != 0)
            i++;
        n = n / i;
        if (n != 1)
            cout << i << "*";
        else
            cout << i << "\n";
    }
    return 0;
}
