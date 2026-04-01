// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M, L;
    cin >> N >> M >> L;
    vector<vector<int>> P(N, vector<int>(M));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> P[i][j];
    vector<int> lowCount(N, 0);
    // Számoljuk, városonként hány roller töltöttsége < L
    for (int i = 0; i < N; i++) {
        int cnt = 0;
        for (int j = 0; j < M; j++) {
            if (P[i][j] < L)
                cnt++;
        }
        lowCount[i] = cnt;
    }
    // Keressük a maximumot
    int maxLow = 0;
    for (int x : lowCount)
        if (x > maxLow)
            maxLow = x;
    // Kiírjuk az eredményt
    cout << maxLow << "\n";
    if (maxLow == 0) {
        cout << "NINCS\n";
        return 0;
    }
    // Az összes várost kiírjuk, ahol maxLow töltöttségű roller van
    bool first = true;
    for (int i = 0; i < N; i++) {
        if (lowCount[i] == maxLow) {
            if (!first)
                cout << " ";
            cout << i + 1; // városok 1-től indexelve
            first = false;
        }
    }
    cout << "\n";
    return 0;
}