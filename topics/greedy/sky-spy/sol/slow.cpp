// @check-accepted: examples small
// @check-time-limit-exceeded: all
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, hanyszor = 0;
    cin >> n;
    vector<int> mikor(n);
    vector<pair<int, int>> idok(n);
    for (int i = 0; i < n; i++) {
        cin >> idok[i].second >> idok[i].first;
    }
    sort(idok.begin(), idok.end());
    for (int i = 0; i < n; i++) {
        if (idok[i].first != 0) {
            mikor[i] = idok[i].first - 1;
            for (int j = i; j < n; j++) {
                if (idok[j].first > mikor[i] && idok[j].second <= mikor[i]) {
                    idok[j].first = 0;
                    idok[j].second = 0;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (mikor[i] != 0) {
            hanyszor++;
        }
    }
    cout << hanyszor << "\n";
    for (int i = 0; i < n; i++) {
        if (mikor[i] != 0) {
            cout << mikor[i] << " ";
        }
    }
}
