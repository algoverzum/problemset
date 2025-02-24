// @check-accepted: *
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> S(n);
    for (int i = 0; i < n; i++) {
        cin >> S[i];
    }
    set<int> A;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        A.insert(x);
    }
    set<int> B;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        B.insert(x);
    }
    int happiness;
    for (auto &cargo : S) {
        if (A.count(cargo)) {
            happiness += 1;
        }
        if (B.count(cargo)) {
            happiness -= 1;
        }
    }
    cout << happiness << "\n";
}
