// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

// Eldönti, hogy a könyvek kioszthatók-e legfeljebb k másolónak úgy,
// hogy senki ne kapjon limit oldalnál többet.
bool ellenoriz(const vector<int> &konyvek, int k, long long limit) {
    int masolok = 1;
    long long aktualis = 0;
    for (int oldal : konyvek) {

        // Egyetlen könyv sem fér bele
        if (oldal > limit)
            return false;

        if (aktualis + oldal <= limit) {
            aktualis += oldal;
        } else {
            masolok++;
            aktualis = oldal;
        }
    }
    return masolok <= k;
}

int main() {

    int n, k;
    cin >> n >> k;

    vector<int> konyvek(n);

    long long bal = 0;
    long long jobb = 0;

    for (int i = 0; i < n; i++) {
        cin >> konyvek[i];

        if (konyvek[i] > bal)
            bal = konyvek[i];

        jobb += konyvek[i];
    }

    long long megoldas = jobb;

    while (bal <= jobb) {
        long long kozep = (bal + jobb) / 2;
        if (ellenoriz(konyvek, k, kozep)) {
            megoldas = kozep;
            jobb = kozep - 1;
        } else {
            bal = kozep + 1;
        }
    }
    cout << megoldas << endl;
    return 0;
}