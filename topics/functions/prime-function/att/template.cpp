#include <iostream>
using namespace std;

// Define a function called prime that returns true if the
// parameter number is a prime and false otherwise.

// Do not change anything below.
int main() {
    for (int i = 1; i <= 1000; i++) {
        if (prime(i))
            cout << i << " ";
    }
    cout << "\n";
}
