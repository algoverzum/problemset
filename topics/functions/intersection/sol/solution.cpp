// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<int> intersection(vector<int> &A, vector<int> &B) {
    vector<int> ans;
    for (int i = 0; i < A.size(); i++) {
        bool ok = false;
        for (int j = 0; j < B.size(); j++) {
            if (A[i] == B[j]) {
                ok = true;
            }
        }
        if (ok) {
            ans.push_back(A[i]);
        }
    }

    return ans;
}

// Do not change anything below!!!
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }
    vector<int> ans;
    ans = intersection(A, B);
    for (auto &num : ans) {
        cout << num << " ";
    }

    cout << "\n";
}
