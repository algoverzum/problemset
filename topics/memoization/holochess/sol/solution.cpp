// @check-accepted: *
#include <iostream>
#include <map>

using namespace std;

map<pair<int, int>, int> memo;

int solv(int x, int y) {
    if (memo.find({x, y}) != memo.end()) {
        return memo[{x, y}];
    }

    int moves[4][2] = {{-2, -1}, {-2, 1}, {1, -2}, {-1, -2}};
    for (auto &move : moves) {
        int stepx = move[0], stepy = move[1];
        if (x + stepx > 0 && y + stepy > 0) {
            int ans = solv(x + stepx, y + stepy);
            if (ans == 2) {
                memo[{x, y}] = 1;
                return 1;
            }
        }
    }

    memo[{x, y}] = 2;
    return 2;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int x, y;
        cin >> x >> y;
        int ans = solv(x, y);
        if (ans == 2) {
            cout << "Second" << endl;
        } else {
            cout << "First" << endl;
        }
    }

    return 0;
}
