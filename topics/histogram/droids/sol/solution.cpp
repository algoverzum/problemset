// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> cnt(11);
    for (int i = 0; i < n; i++) {
        int type;
        cin >> type;
        cnt[type]++;
    }
    int maxi = 0;
    for (int i = 1; i < 11; i++) {
        maxi = max(maxi, cnt[i]);
    }
    cout << maxi << "\n";
}
