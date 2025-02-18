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
    vector<int> ans;
    for (int i = 1; i < n - 1; i++) {
        if (2 * A[i] == A[i - 1] + A[i + 1]) {
            ans.push_back(A[i]);
        }
    }
    cout << ans.size() << "\n";
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << "\n";
}
