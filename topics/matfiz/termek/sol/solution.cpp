// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int E, N, K;
    cin >> E >> N >> K;
    vector<vector<int>> floors(E, vector<int>(N));
    vector<int> sums(E, 0);
    for (int i = 0; i < E; i++) {
        for (int j = 0; j < N; j++) {
            cin >> floors[i][j];
            sums[i] += floors[i][j]; // soronkénti összegzés
        }
    }
    // Legkisebb összegű szint kiválasztása
    int best = 0;
    for (int i = 1; i < E; i++)
        if (sums[i] < sums[best])
            best = i;
    // A best szint teremlétszámai rendezve
    vector<int> rooms = floors[best];
    sort(rooms.begin(), rooms.end());

    cout << best + 1 << "\n";
    for (int x : rooms)
        cout << x << " ";
    cout << "\n";
}