#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<vector<int>> elek;
vector<int> db;
vector<vector<long long int>> pas;
vector<long long int> fele;

void darab(int a) {
    int sum = 0;
    for (int i : elek[a]) {
        darab(i);
        sum += (db[i] % 1000000007);
    }
    sum++;
    db[a] = (sum % 1000000007);
}

void megold(int a) {
    long long int sum = 1;
    int db1 = db[a] - 1;
    for (int i : elek[a]) {
        megold(i);
        sum = (sum * fele[i] % 1000000007);
        sum = ((sum * pas[db1][db[i]]) % 1000000007);
        db1 -= db[i];
    }
    fele[a] = sum;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int n;
    cin >> n;
    elek.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        int db;
        cin >> db;
        for (int j = 1; j <= db; j++) {
            int a;
            cin >> a;
            elek[i].push_back(a);
        }
    }
    db.resize(n + 1);
    pas.resize(n);
    pas[0].push_back(1);
    for (int i = 1; i <= n - 1; i++) {
        pas[i].resize(i + 1, 0);
        pas[i][0] = 1;
        for (int j = 1; j < i; j++) {
            pas[i][j] = (pas[i - 1][j - 1] + pas[i - 1][j]) % 1000000007;
        }
        pas[i][i] = 1;
    }
    darab(1);
    fele.resize(n + 1);
    megold(1);
    cout << fele[1];
    return 0;
}
