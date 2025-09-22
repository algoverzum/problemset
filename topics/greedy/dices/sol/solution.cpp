// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> S(n);
    for (int i = 0; i < n; i++) {
        cin >> S[i];
    }

    sort(S.begin(), S.end());

    int length = 0;
    for (int si : S) {
        if (si > length) {
            length++;
        }
    }

    cout << length << "\n";
    return 0;
}
