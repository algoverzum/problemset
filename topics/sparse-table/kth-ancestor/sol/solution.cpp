#include <bits/stdc++.h>
using namespace std;

int kthancestor(vector<vector<int>> &v, int x, int k) {
    for (int i = 0; i < 19 && x != -1; i++) {
        if (k & (1 << i)) {
            x = v[x][i];
        }
    }
    return x;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> v(n + 1, vector<int>(19, -1));
    int q;
    cin >> q;
    int type, y, x, k;

    for (int i = 0; i < q; i++) {
        cin >> type;
        if (type == 0) {
            cin >> y >> x;
            v[x][0] = y;
            for (int j = 1; j < 19; j++) {
                if (v[x][j - 1] != -1) {
                    v[x][j] = v[v[x][j - 1]][j - 1];
                } else {
                    break;
                }
            }
        } else if (type == 1) {
            cin >> x;
            v[x][0] = -1;
            for (int j = 1; j < 19; j++) {
                v[x][j] = -1;
            }
        } else if (type == 2) {
            cin >> x >> k;
            int ancestor = kthancestor(v, x, k);
            if (ancestor == -1)
                ancestor = 0;
            cout << ancestor << endl;
        }
    }
    return 0;
}
