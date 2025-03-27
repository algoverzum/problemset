// @check-accepted: *
#include <iostream>
#include <unordered_set>
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
    unordered_set<int> A;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        A.insert(x);
    }
    unordered_set<int> B;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        B.insert(x);
    }
    int happiness = 0;
    for (int cargo : S) {
        if (A.count(cargo)) {
            happiness += 1;
        }
        if (B.count(cargo)) {
            happiness -= 1;
        }
    }
    cout << happiness << "\n";
}
