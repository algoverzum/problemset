// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// Döntési függvény: megvizsgálja, hogy elengedő-e K darab R hatósugarú állomás
bool check(long long R, int N, int K, const vector<long long> &a) {
    int stations_used = 0;
    int i = 0;

    while (i < N) {
        // Elhasználunk egy állomást a jelenlegi legelső lefedetlen faluhoz
        // (a[i])
        stations_used++;

        // Ha több állomás kellene, mint amennyi van, ez az R hatósugár nem elég
        if (stations_used > K)
            return false;

        // Megkeressük, meddig tud elnyúlni ez az állomás.
        // A maximális távolság a legelső lefedett falu és a legtávolabbi között
        // 2 * R lehet.
        long long max_reach = a[i] + 2 * R;

        // Mohón eltoljuk az indexet a következő olyan faluig, ami már kívül
        // esik ezen a hatókörön
        while (i < N && a[i] <= max_reach) {
            i++;
        }
    }

    return stations_used <= K;
}

int main() {
    // Gyors I/O a hatékonyság érdekében
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K))
        return 0;

    vector<long long> a(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }

    // Parametrikus (bináris) keresés a minimális R hatósugárra
    long long low = 0;
    long long high = a[N - 1] - a[0];
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;

        if (check(mid, N, K, a)) {
            ans = mid; // R=mid lehetséges, elmentjük mint eddigi legkisebb
                       // hatósugár
            high = mid - 1; // Megpróbálunk még kisebb hatósugarat találni
        } else {
            low =
                mid + 1; // Ha mid nem elég, nagyobb hatósugárra van szükségünk
        }
    }

    cout << ans << "\n";

    return 0;
}