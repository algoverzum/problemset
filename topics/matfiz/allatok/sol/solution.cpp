// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    vector<vector<int>> E(M, vector<int>(N));

    // Bemenet
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            cin >> E[i][j];

    // Minden oszlopra külön-külön meghatározzuk a maxot és az első helyet
    for (int j = 0; j < N; j++) {
        int maxVal = -1;
        int bestPark = 1; // 1-től indexelve

        for (int i = 0; i < M; i++) {
            if (E[i][j] > maxVal) {
                maxVal = E[i][j];
                bestPark = i + 1;
            }
        }

        cout << bestPark;
        if (j < N - 1)
            cout << " ";
    }

    cout << endl;
    return 0;
}
