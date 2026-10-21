// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    // Gyorsítjuk a standard I/O műveleteket
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N, L, K;
    if (!(cin >> N >> L >> K))
        return 0;

    // Beolvassuk a kezdeti darabszámokat (1-től L éves korig)
    vector<long long> kezdeti_populacio(L);
    for (int i = 0; i < L; ++i) {
        cin >> kezdeti_populacio[i];
    }

    // A sort fordított sorrendben töltjük fel:
    // A sor elején (front) a legidősebb (L éves), a végén (back) a legfiatalabb
    // (1 éves) lesz.
    queue<long long> roka_sor;
    for (int i = L - 1; i >= 0; --i) {
        roka_sor.push(kezdeti_populacio[i]);
    }

    // Évek szimulációja N éven keresztül
    for (int ev = 0; ev < N; ++ev) {
        long long ujszulottek = 0;

        // Lemásoljuk a sort, hogy végig tudjuk számolni a szaporodókat
        queue<long long> masolat = roka_sor;

        // Kiszámoljuk a születő rókákat.
        // Mivel fordított a sorrend, a sor legelső (L - K + 1) eleme
        // szaporodóképes.
        int szaporodo_korcsoportok = L - K + 1;
        for (int i = 0; i < szaporodo_korcsoportok; ++i) {
            ujszulottek = (ujszulottek + masolat.front()) % 1000000;
            masolat.pop();
        }

        // 1. Az L évesek elpusztulnak (kivesszük őket a sor elejéről)
        roka_sor.pop();

        // 2. Az újszülöttek bekerülnek a sor végére (mint 1 évesek)
        roka_sor.push(ujszulottek);
    }

    // Végeredmény kiszámítása: összeadjuk a sorban maradt összes rókát
    long long osszes_roka = 0;
    while (!roka_sor.empty()) {
        osszes_roka = (osszes_roka + roka_sor.front()) % 1000000;
        roka_sor.pop();
    }

    // Kimenet a feladat által kért formátumban
    cout << osszes_roka << "\n";

    return 0;
}
