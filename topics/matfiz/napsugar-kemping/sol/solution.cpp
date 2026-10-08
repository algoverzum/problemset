// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int K, M, N;
    cin >> K >> M >> N;

    vector<int> igenyek(366, 0); // 1..365 napok
    for (int i = 0; i < N; i++) {
        int nap;
        cin >> nap;
        igenyek[nap]++;
    }

    vector<int> fszabad(K + 1, 0); // 1..K faházak
    int megold = 0;

    for (int nap = 1; nap <= 365; nap++) {
        while (igenyek[nap] > 0) {
            // Keresünk egy szabad faházat
            int j = 1;
            while (j <= K && fszabad[j] > nap) {
                j++;
            }

            if (j <= K) {
                megold++;
                igenyek[nap]--;
                fszabad[j] = nap + M;
            } else {
                break; // Nincs szabad faház ezen a napon
            }
        }
    }

    cout << megold << endl;

    return 0;
}

/* Alternatív megoldás
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int K, M, N;
    cin >> K >> M >> N;

    vector<int> igenyek(N);
    for (int i = 0; i < N; i++) {
        cin >> igenyek[i];
    }

    // Rendezés a kezdőnap szerint
    sort(igenyek.begin(), igenyek.end());

    // A faházakban azt tároljuk, hogy az adott faházban mikor szabadul fel a
következő nap
    // Kezdetben minden faház szabad (0. naptól)
    vector<int> fahazak(K, 0);

    int elfogadott = 0;

    for (int i = 0; i < N; i++) {
        int kezdet = igenyek[i];

        // Megkeressük a legkorábban felszabaduló faházat
        int legkorabbi_index = 0;
        for (int j = 1; j < K; j++) {
            if (fahazak[j] < fahazak[legkorabbi_index]) {
                legkorabbi_index = j;
            }
        }

        // Ha a legkorábban felszabaduló faház már szabad a kezdetkor
        if (fahazak[legkorabbi_index] <= kezdet) {
            elfogadott++;
            // A faház a kezdet + M nap múlva szabadul fel
            fahazak[legkorabbi_index] = kezdet + M;
        }
        // Különben nem tudjuk elfogadni ezt az igényt (nincs szabad faház)
    }

    cout << elfogadott << endl;

    return 0;
}
*/