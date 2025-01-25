#define CMS
#include "string"
#include "testlib.h"
#include "vector"
using namespace std;

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);

    int goodans = ans.readInt();
    int userans = ouf.readInt();

    if (goodans != userans)
        quit(_wa, "wrong");

    int n = inf.readInt();
    int m = inf.readInt();
    vector<vector<int>> cells(n + 1, vector<int>(m + 1, -1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cells[i][j] = inf.readInt();
        }
    }

    if (userans == -1)
        quit(_ok, "ok");

    ouf.readEoln();
    string s = ouf.readString();
    int x = 0, y = 0, cur = cells[0][0];

    if (s.size() != n + m - 2)
        quitp(0.5, "wrong length");

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'R') {
            x += 1;
            if (x >= m)
                quitp(0.5, "out of board");
            if (cells[y][x] == -1)
                quitp(0.5, "trap");
            cur += cells[y][x];
        } else if (s[i] == 'D') {
            y += 1;
            if (y >= n)
                quitp(0.5, "out of board");
            if (cells[y][x] == -1)
                quitp(0.5, "trap");
            cur += cells[y][x];
        } else {
            quitp(0.5, "wrong char (not D or R)");
        }
    }

    if (cur == goodans) {
        quit(_ok, "ok");
    } else {
        quitp(0.5, "wrong path");
    }
    return 0;
}
