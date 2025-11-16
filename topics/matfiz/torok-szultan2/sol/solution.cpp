// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;
int main() {
    int N;
    cin >> N;
    vector<bool> cella(N + 1, false);
    for (int szolga = 1; szolga <= N; szolga++) {
        for (int rab = szolga; rab <= N; rab += szolga) {
            cella[rab] = not cella[rab];
        }
    }
    for (int i = 1; i <= N; i++) {
        if (cella[i])
            cout << i << " ";
    }
    cout << "\n";
    return 0;
}
