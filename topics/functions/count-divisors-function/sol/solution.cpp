// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

// Create a count_divisors function here
int count_divisors(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            count++;
        }
    }
    return count;
}

// Do not change anything below!!!
int main() {
    int num;
    cin >> num;
    cout << count_divisors(num) << "\n";
}