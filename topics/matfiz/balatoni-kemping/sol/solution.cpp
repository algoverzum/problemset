// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

// Foglalási igény: kezdőnap és az a nap, amikor a faház újra szabad
struct Igeny {
    int start;
    int end; // t + h: ezen a napon a faház már szabad
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int D, K, N;
    if (!(cin >> D >> K >> N))
        return 0;

    vector<Igeny> igenyek(N);
    for (int i = 0; i < N; ++i) {
        int t, h;
        cin >> t >> h;
        igenyek[i] = {t, t + h};
    }

    // 1. Rendezés végnap szerint (egyenlőség esetén kezdőnap szerint,
    //    hogy a futás determinisztikus legyen)
    sort(igenyek.begin(), igenyek.end(), [](const Igeny &a, const Igeny &b) {
        if (a.end != b.end)
            return a.end < b.end;
        return a.start < b.start;
    });

    // 2. A faházak felszabadulási napjai rendezett multihalmazban.
    //    Kezdetben mind a K faház üres: felszabadulási napjuk 0.
    multiset<int> fahazak;
    for (int i = 0; i < K; ++i)
        fahazak.insert(0);

    int elfogadott_db = 0;

    for (const auto &ig : igenyek) {
        // Az első olyan faház, amely az igény kezdete UTÁN szabadul fel
        auto it = fahazak.upper_bound(ig.start);
        if (it == fahazak.begin())
            continue; // egyik faház sem szabad: elutasítjuk
        --it;         // a LEGKÉSŐBB felszabaduló, de már szabad faház
        fahazak.erase(it);
        fahazak.insert(ig.end);
        ++elfogadott_db;
    }

    cout << elfogadott_db << "\n";
    return 0;
}
