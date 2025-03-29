#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> res;
    for (int i = 0; i < n; i++) {
        int d, p;
        cin >> d >> p;
        if (p <= 100 * d) {
            res.push_back(i + 1);
        }
    }
    cout << res.size() << "\n";
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << ' ';
    }
}
