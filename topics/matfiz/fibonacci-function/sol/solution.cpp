// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

void fibonacci(vector<long long> &fib, int n) {
    fib.push_back(0);
    fib.push_back(1);
    for (int i = 2; i < n; i++) {
        fib.push_back(fib[i - 1] + fib[i - 2]);
    }
}

int main() {
    int n;
    cin >> n;
    vector<long long> t;
    fibonacci(t, n);
    for (long long x : t)
        cout << x << " ";
    cout << "\n";
}
