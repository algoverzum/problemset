#include <bits/stdc++.h>
using namespace std;

int N, M;

vector<vector<int>> forbidden;
vector<int> current, best;

/*
Ellenőrzi, hogy az új torony felvehető-e
a jelenlegi kiválasztottak mellé.
*/
bool ok(int x) {
    for (int y : current) {
        for (int z : forbidden[y]) {
            if (z == x) return false;
        }
    }
    return true;
}

/* Lexikografikus összehasonlítás: true, ha a < b */
bool lexicographicallySmaller(const vector<int> &a, const vector<int> &b) {
    return a < b;
}

/* Pruning: megnézzük, hogy van-e esély jobb megoldásra*/
bool canImprove(int idx, int currentSize) {
    int remaining = N - idx + 1;
    return currentSize + remaining >= (int)best.size();
}

void backtrack(int idx) {
    if (idx > N) {
        if (current.size() > best.size()) {
            best = current;
        } 
        else if (current.size() == best.size()) {
            if (lexicographicallySmaller(current, best)) {
                best = current;
            }
        }
        return;
    }

    // PRUNING: ha innen már nem lehet jobb megoldás
    if (!canImprove(idx, current.size())) {
        return;
    }

    // 1. ág: NEM választjuk
    backtrack(idx + 1);

    // 2. ág: választjuk (ha lehet)
    if (ok(idx)) {
        current.push_back(idx);
        backtrack(idx + 1);
        current.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    forbidden.assign(N + 1, vector<int>());

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        forbidden[a].push_back(b);
        forbidden[b].push_back(a);
    }

    backtrack(1);

    cout << best.size() << "\n";

    for (int i = 0; i < (int)best.size(); i++) {
        cout << best[i];
        if (i + 1 < (int)best.size()) cout << " ";
    }
    cout << "\n";

    return 0;
}
