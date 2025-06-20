// @check-accepted: *

#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

int R, C;
vector<string> grid;
map<tuple<int, int, int, int>, int> memo;

int mex(const set<int> &s) {
    int m = 0;
    while (s.count(m))
        m++;
    return m;
}

bool is_row_empty(int r, int c1, int c2) {
    for (int c = c1; c < c2; ++c) {
        if (grid[r][c] != '.')
            return false;
    }
    if (c1 < c2)
        return true;
    return false;
}

bool is_col_empty(int c, int r1, int r2) {
    for (int r = r1; r < r2; ++r) {
        if (grid[r][c] != '.')
            return false;
    }
    if (r1 < r2)
        return true;
    return false;
}

int grundy(int r1, int r2, int c1, int c2) {
    auto key = make_tuple(r1, r2, c1, c2);
    if (memo.count(key))
        return memo[key];

    set<int> gset;

    for (int r = r1; r < r2; ++r) {
        if (is_row_empty(r, c1, c2)) {
            int top = grundy(r1, r, c1, c2);
            int bottom = grundy(r + 1, r2, c1, c2);
            gset.insert(top ^ bottom);
        }
    }

    for (int c = c1; c < c2; ++c) {
        if (is_col_empty(c, r1, r2)) {
            int left = grundy(r1, r2, c1, c);
            int right = grundy(r1, r2, c + 1, c2);
            gset.insert(left ^ right);
        }
    }

    int result = mex(gset);
    memo[key] = result;
    return result;
}

int main() {
    cin >> R >> C;
    grid.resize(R);
    for (int i = 0; i < R; ++i) {
        cin >> grid[i];
    }

    int g = grundy(0, R, 0, C);
    cout << (g != 0 ? "Becca" : "Terry") << "\n";
    return 0;
}
