#include <bits/stdc++.h>
#include <iostream>
using namespace std;

const int p = 1000000007;

vector<vector<int>> elek;
vector<int> db;
vector<vector<long long int>> pas;
vector<long long int> fele;
vector<long long int> fact;

void darab(int a) {
    int sum = 0;
    for (int i : elek[a]) {
        darab(i);
        sum += db[i];
    }
    sum++;
    db[a] = sum;
}

void megold(int a) {
    long long int sum = 1;
    int db1 = db[a] - 1;
    for (int i : elek[a]) {
        megold(i);
        sum = (sum * fele[i] % p);
        sum = ((sum * pas[db1][db[i]]) % p);
        db1 -= db[i];
    }
    fele[a] = sum;
}

long long int hatvany(int n, int k, int m) {
    int i = k;
    long long szor = 1;
    long long hat = n;
    while (i > 0) {
        if (i % 2 == 1) {
            szor = (szor * hat) % m;
        }
        hat = (hat * hat) % m;
        i = i / 2;
    }
    return szor;
}

void megold2(int a) {
    long long int sum = 1;
    int db1 = db[a] - 1;
    sum = sum * fact[db1] % p;
    for (int i : elek[a]) {
        megold2(i);
        sum = sum * fele[i] % p;
        sum = sum * hatvany(fact[db[i]], p - 2, p) % p;
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
    /*pas.resize(n);
    pas[0].push_back(1);
    for(int i=1; i<=n-1; i++)
    {
        pas[i].resize(i+1,0);
        pas[i][0]=1;
        for(int j=1;j<i; j++)
        {
            pas[i][j]=(pas[i-1][j-1]+pas[i-1][j])%p;
        }
        pas[i][i]=1;
    }*/
    fact.resize(n + 1);
    fact[0] = 1;
    fact[1] = 1;
    for (int i = 2; i <= n; i++) {
        fact[i] = (fact[i - 1] * i) % p;
    }

    darab(1);
    fele.resize(n + 1);
    megold2(1);
    cout << fele[1];
    return 0;
}
