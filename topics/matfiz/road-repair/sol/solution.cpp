// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {

    int N, M;
    cin >> N >> M;

    vector<int> lengths(M);
    int K, V;

    for (int i = 0; i < M; i++) {
        cin >> K >> V;
        lengths[i] = V - K + 1; // hossz km-ben
    }

    // minimum hossz keresése
    int minLen = lengths[0];
    for (int i = 1; i < M; i++) {
        if (lengths[i] < minLen)
            minLen = lengths[i];
    }

    // kiírás
    cout << minLen << "\n";
    for (int i = 0; i < M; i++) {
        if (lengths[i] == minLen)
            cout << (i + 1) << "\n"; // sorszám 1-től
    }

    return 0;
}
