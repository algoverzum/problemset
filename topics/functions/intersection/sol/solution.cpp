// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<int> intersection(vector<int> a, vector<int> b) {
    vector<int> common;
    for (int i = 0; i < a.size(); i++) {
        bool found = false;
        for (int j = 0; j < b.size(); j++) {
            if (a[i] == b[j]) {
                found = true;
            }
        }
        if (found) {
            common.push_back(a[i]);
        }
    }

    return common;
}

// Do not change anything below!!!
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
