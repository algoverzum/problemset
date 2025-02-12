// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 1; i < n - 1; i++) {
        if (2 * A[i] == A[i - 1] + A[i + 1]) {
            cout << A[i] << " ";
        }
    }
    cout << "\n";
}
