// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    int maxdiff = B[0] - A[0];
    for (int i = 0; i < n; i++) {
        maxdiff = max(maxdiff, B[i] - A[i]);
    }
    cout << maxdiff << "\n";
}
