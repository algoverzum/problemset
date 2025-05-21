// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector<bool> win(N + 12, true);
        for (int i = N; i >= 0; i--) {
            win[i] = !win[i + 4] || !win[i + 5] || !win[i + 11];
        }
        cout << (win[0] ? "R2-D2\n" : "C-3PO\n");
    }

    return 0;
}
