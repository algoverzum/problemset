#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;

long long mod_pow(long long a, long long e, long long m = MOD) {
    long long r = 1;
    while (e > 0) {
        if (e & 1)
            r = (r * a) % m;
        a = (a * a) % m;
        e >>= 1;
    }
    return r;
}

int n;
vector<vector<int>> children;
vector<int> subtree_size;
vector<long long> ways;
vector<long long> fact, invfact;

int dfs_size(int u) {
    int sum = 1;
    for (int v : children[u])
        sum += dfs_size(v);
    return subtree_size[u] = sum;
}

long long dfs_ways(int u) {
    // ways[u] = ( (sum)! / Π (size[v])! ) * Π ways[v],
    // ahol sum = Σ size[v] a gyerekekre
    long long prod = 1;
    int sum_sizes = 0;
    for (int v : children[u]) {
        prod = (prod * dfs_ways(v)) % MOD;
        prod =
            (prod * invfact[subtree_size[v]]) % MOD; // osztás fact(size[v])-val
        sum_sizes += subtree_size[v];
    }
    return ways[u] = fact[sum_sizes] * prod % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    children.resize(n + 1);
    for (int u = 1; u <= n; ++u) {
        int k;
        cin >> k;
        children[u].reserve(k);
        for (int j = 0; j < k; ++j) {
            int v;
            cin >> v;
            children[u].push_back(v);
        }
    }

    // Előfeldolgozás: fact, invfact
    fact.resize(n + 1);
    invfact.resize(n + 1);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i)
        fact[i] = fact[i - 1] * i % MOD;
    invfact[n] = mod_pow(fact[n], MOD - 2);
    for (int i = n; i >= 1; --i)
        invfact[i - 1] = invfact[i] * i % MOD;

    subtree_size.assign(n + 1, 0);
    ways.assign(n + 1, 0);

    dfs_size(1);
    cout << dfs_ways(1) % MOD << '\n';
    return 0;
}
