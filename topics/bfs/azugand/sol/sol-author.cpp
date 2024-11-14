// @check-accepted: examples NQsmall Qsmall Bsmall full
#include <bits/stdc++.h>

using namespace std;

const long long max_size = 2e5 + 100, INF = 2e9 + 2, mod = 1e9 + 7, max_c = (1 << 18) + 2;

int v[max_size], dist[21][max_size];
vector <pair <int, int>> adj[max_size];

void bfs01 (int bit, int start)
{
    deque <int> dq;
    dq.push_back(start);
    dist[bit][start] = 0;
    while (!dq.empty())
    {
        int nod = dq.front();
        dq.pop_front();
        for (auto f : adj[nod])
        {
            if (dist[bit][f.first] == INF)
            {
                dist[bit][f.first] = dist[bit][nod] + f.second;
                if (f.second == 0)
                {
                    dq.push_front(f.first);
                }
                else
                {
                    dq.push_back(f.first);
                }
            }
        }
    }
}

void solve()
{
    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
    {
        cin >> v[i];
        for (int e = 0; e <= 20; e++)
        {
            if ((v[i] & (1 << e)) != 0)
            {   
                adj[i].push_back({n + e + 1, 0});
                adj[n + e + 1].push_back({i, 1});
            }
        }
    }
    for (int i = 1; i <= n + 21; i++)
    {
        for(int j = 0; j <= 20; j++)
        {
            dist[j][i] = INF;
        }
    }
    for (int j = 0; j <= 20; j++)
    {
        bfs01(j, n + j + 1);
    }
    while (q--)
    {
        int ans = INF, x, y;
        cin >> x >> y;
        for (int j = 0; j <= 20; j++)
        {
            if(v[x]&(1<<j)) ans = min(ans, dist[j][y]);
        }
        cout << (ans == INF ? -1 : ans) << '\n';
    }
    cout << '\n';
}

signed main()
{
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#endif // LOCAL
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long tt;
    // cin >> tt;
    tt = 1;
    while (tt--)
    {
        solve();
    }
    return 0;
}
