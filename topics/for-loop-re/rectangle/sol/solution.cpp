// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cout << 'X';
        }
        cout << "\n";
    }
    return 0;
}
