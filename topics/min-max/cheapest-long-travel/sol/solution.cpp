// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    vector<int> B(n);
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    int result = -1;
    for (int i = 0; i < n; i++) {
        if (A[i] >= k) {
            if (result < B[i]) {
                result = B[i];
            }
            if (result == -1) {
                result = B[i];
            }
        }
    }
    cout << result << "\n";
    return 0;
}
