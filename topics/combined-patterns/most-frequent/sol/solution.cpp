// @check-accepted: *
#include <algorithm>
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
    int mostFrequent = A[0], Count = 1;
    for (int i = 0; i < n; i++) {
        int c = count(A.begin(), A.end(), A[i]);
        if (c > Count) {
            mostFrequent = A[i];
            Count = c;
        } else if (c == Count) {
            if (mostFrequent > A[i]) {
                mostFrequent = A[i];
            }
        }
    }

    cout << mostFrequent << "\n";
}
