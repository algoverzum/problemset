// @check-zero: small
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b;
    cin >> a >> b;

    int max_len = 0;
    for (int i = 0; i < a.size(); i++) {
        int len = 0;
        for (int j = 0; j < b.size(); j++) {
            if (a[i + len] == b[j])
                len++;
            else {
                max_len = max(max_len, len);
                len = 0;
            }
        }
        max_len = max(max_len, len);
    }

    cout << max_len;

    return 0;
}
