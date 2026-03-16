#include <iostream>
#include <vector>
using namespace std;

// Define a function called fibonacci here.

// Do not change anything below.
int main() {
    int n;
    cin >> n;
    vector<long long> t;
    fibonacci(t, n);
    for (long long x : t)
        cout << x << " ";
}
