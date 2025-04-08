#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, e, a, r;
    cin >> n >> m >> r;
    vector<vector<int>> v(n + 1);
    vector<int> honnan(n + 1), tav(n + 1, -1);
    tav[r] = 0;
    queue<int> q;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> b >> a;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int minhossz = n + 1;
    q.push(r);
    while (!q.empty()) {
        int cs = q.front();
        q.pop();
        for (int x : v[cs]) {
            if (tav[x] == -1) {
                q.push(x);
                tav[x] = tav[cs] + 1;
                honnan[x] = cs;
            } else {
                if (tav[x] >= tav[cs] && minhossz > tav[x] + tav[cs] + 1) {
                    minhossz = tav[x] + tav[cs] + 1;
                    e = x;
                    a = cs;
                }
            }
        }
    }
    if (minhossz == n + 1) {
        cout << "-1";
        return 0;
    }
    int x = e, y = a;
    cout << minhossz << endl;
    vector<int> ut;
    ut.push_back(e);
    while (x != r) {
        ut.push_back(honnan[x]);
        x = honnan[x];
    }
    for (int i = ut.size() - 1; i >= 0; i--) {
        cout << ut[i] << " ";
    }
    cout << a << ' ';
    while (honnan[y] != r) {
        cout << honnan[y] << ' ';
        y = honnan[y];
    }
    return 0;
}