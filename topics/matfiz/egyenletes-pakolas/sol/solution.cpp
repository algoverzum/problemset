// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N, K;
vector<int> sulyok;

// Ellenőrzi, hogy X maximális terhelés mellett
// el lehet-e osztani a konténereket legfeljebb K kamionba
bool lehet(long long X, vector<int> *kezdo_indexek = nullptr) {
    int kamionok = 1;
    long long aktualis = 0;

    if (kezdo_indexek != nullptr) {
        kezdo_indexek->clear();
        kezdo_indexek->push_back(1);
    }

    for (int i = 0; i < N; i++) {
        if (aktualis + sulyok[i] > X || (N - i) <= (K - kamionok)) {
            kamionok++;
            aktualis = sulyok[i];
            if (kezdo_indexek != nullptr) {
                kezdo_indexek->push_back(i + 1);
            }
        } else {
            aktualis += sulyok[i];
        }
        if (kamionok > K) {
            return false;
        }
    }

    return true;
}

int main() {
    cin >> N >> K;
    sulyok.resize(N);

    long long bal = 0, jobb = 0;
    for (int i = 0; i < N; i++) {
        cin >> sulyok[i];
        bal = max(bal, (long long)sulyok[i]);
        jobb += sulyok[i];
    }

    // Paraméteres keresés (bináris keresés) a minimális maximumra
    while (bal < jobb) {
        long long kozep = (bal + jobb) / 2;
        if (lehet(kozep)) {
            jobb = kozep;
        } else {
            bal = kozep + 1;
        }
    }

    long long optimum = bal;
    cout << optimum << endl;

    // Kezdőindexek meghatározása
    vector<int> kezdo_indexek;
    lehet(optimum, &kezdo_indexek);

    if (kezdo_indexek.size() != K) {
        cout << "hiba: " << kezdo_indexek.size() << " != " << K << endl;
        return 1;
    }

    for (int i = 0; i < K; i++) {
        cout << kezdo_indexek[i] << " ";
    }
    cout << endl;

    return 0;
}
