// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<bool> prim(N + 1, true);
    for (int i = 2; i <= N; i++) {
        if (prim[i]) {
            for (int j = i; i * j <= N; j++)
                prim[i * j] = false;
        }
    }
    for (int i = 2; i <= N; i++)
        if (prim[i])
            cout << i << ' ';
    cout << "\n";
    return 0;
}
