// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    int ans = 0;
    for (int i = 0; i < N / 2; ++i) {
        ans += A[2 * i + 1] - A[2 * i];
    }

    cout << ans << '\n';
    return 0;
}
