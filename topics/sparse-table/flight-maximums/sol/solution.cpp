// @check-accepted: *
#include <iostream>
using namespace std;

const int MAXN = 1e5;
const int MAXK = 17;
int lg[MAXN + 1];
int st[MAXK + 1][MAXN + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    lg[1] = 0;
    for (int i = 2; i <= MAXN; i++)
        lg[i] = lg[i / 2] + 1;

    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++)
        cin >> st[0][i];

    for (int i = 1; i <= lg[n]; i++)
        for (int j = 1; j + (1 << i) - 1 <= n; j++)
            st[i][j] = max(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);

    while (q--) {
        int s, k;
        cin >> s >> k;
        cout << st[k][s] << "\n";
    }

    return 0;
}
