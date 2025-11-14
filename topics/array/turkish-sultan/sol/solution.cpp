// @check-accepted: *
#include <iostream>
#include <vector>

#define ZAR 0
#define NYIT 1
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> cella(N + 1);
    for (int rab = 1; rab <= N; rab++) {
        for (int szolga = 1; szolga <= N; szolga++) {
            if (rab % szolga == 0)
                cella[rab] = 1 - cella[rab];
        }
    }
    for (int i = 1; i <= N + 1; i++) {
        if (cella[i] == NYIT)
            cout << i << ' ';
    }
    cout << "\n";
    return 0;
}
