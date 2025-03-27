// @check-accepted: examples
// @check-time-limit-exceeded: all
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> S(n);
    for (int i = 0; i < n; i++) {
        cin >> S[i];
    }
    vector<int> A(m);
    for (int i = 0; i < m; i++) {
        cin >> A[i];
    }
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }
    int happiness = 0;
    for (int cargo : S) {
        if (find(A.begin(), A.end(), cargo) != A.end()) {
            happiness += 1;
        }
        if (find(B.begin(), B.end(), cargo) != B.end()) {
            happiness -= 1;
        }
    }
    cout << happiness << "\n";
}
