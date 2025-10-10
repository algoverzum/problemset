// @check-accepted: *
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    int n = S.size();

    int Q;
    cin >> Q;

    vector<int> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + (isVowel(S[i - 1]) ? 1 : 0);
    }

    while (Q--) {
        int i, j;
        cin >> i >> j;
        cout << prefix[j] - prefix[i - 1] << "\n";
    }

    return 0;
}
