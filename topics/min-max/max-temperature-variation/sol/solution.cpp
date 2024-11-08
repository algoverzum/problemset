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
    vector<int> B(n);
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    int result = B[0] - A[0];
    for (int i = 0; i < n; i++) {
        int current = B[i] - A[i];
        if (result < current) {
            result = current;
        }
    }
    cout << result << "\n";
}
