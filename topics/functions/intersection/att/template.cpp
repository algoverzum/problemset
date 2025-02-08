#include <bits/stdc++.h>
using namespace std;

vector<int> intersection(vector<int> &A, vector<int> &B) {

    // Write your code here

    return vector<int>();
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
