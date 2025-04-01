#include <bits/stdc++.h>
using namespace std;

// Define a function called intersection here.

// Do not change anything below.
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<int> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    vector<int> ans = intersection(a, b);
    for (int num : ans) {
        cout << num << " ";
    }
    cout << "\n";
}
