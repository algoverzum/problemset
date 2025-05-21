// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

int memo[101][101];

int winner(int x, int y) {
    if (x < 1 || x > 100 || y < 1 || y > 100)
        return 1;
    if (memo[x][y] != 0) {
        return memo[x][y];
    }

    vector<pair<int, int>> moves = {{-2, -1}, {-2, 1}, {1, -2}, {-1, -2}};
    for (auto [stepx, stepy] : moves) {
        if (winner(x + stepx, y + stepy) == 2) {
            return memo[x][y] = 1;
        }
    }

    return memo[x][y] = 2;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int x, y;
        cin >> x >> y;
        if (winner(x, y) == 2) {
            cout << "Second\n";
        } else {
            cout << "First\n";
        }
    }
}
