// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> A(n), B(m);

    for (int i = 0; i < n; i++)
        cin >> A[i];

    for (int i = 0; i < m; i++)
        cin >> B[i];

    int ans = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (A[i] + B[j] <= k)
                ans++;
        }
    }

    cout << ans << '\n';
    return 0;
}
