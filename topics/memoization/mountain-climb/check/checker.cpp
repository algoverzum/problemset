#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int>> mountain;
vector<vector<int>> memo;
vector<pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int rec(int i, int j) {
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    int height = mountain[i][j];
    int ret = 0;
    for (auto [di, dj] : moves) {
        if (mountain[i + di][j + dj] == height + 1) {
            ret = max(ret, rec(i + di, j + dj) + 1);
        }
    }
    return memo[i][j] = ret;
}

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt(); // read input
    inf.readEoln();
    mountain.assign(N + 2, vector<int>(N + 2, -1));
    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            mountain[i][j] = inf.readInt();
        }
        // inf.readEoln();
    }

    int opt_sol = ans.readInt(); // official solution, first line is enough

    // user solution:
    int user_sol = ouf.readInt();
    ouf.readEoln();
    int row = ouf.readInt();
    int col = ouf.readInt();
    // ouf.readEoln();

    // check ans first line
    if (user_sol != opt_sol) {
        quitf(
            _wa,
            "Not optimal solution: %d found, but optimal solution has %d steps",
            user_sol, opt_sol);
    }

    // Solve
    memo.assign(N + 2, vector<int>(N + 2, -1));
    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            rec(i, j);
        }
    }

    if (row == 1 || row == N || col == 1 || col == N) {
        if (memo[row][col] == user_sol) {
            quitf(_ok, "Correct Answer");
        } else {
            quitf(_wa, "Wrong Answer");
        }
    } else {
        quitf(_wa, "Cell not on boundary");
    }
}
