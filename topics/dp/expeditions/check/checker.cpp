#define CMS
#include "testlib.h"
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;
struct Permit {
    int start, end, credits;
};

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    int m = inf.readInt();
    inf.readEoln();
    vector<Permit> permits(n + 2);
    for (int i = 1; i <= n; i++) {
        permits[i].start = inf.readInt();
        permits[i].end = inf.readInt();
        permits[i].credits = inf.readInt();
        inf.readEoln();
    }
    int opt_K = ans.readInt();

    int user_income = ouf.readInt();
    ouf.readEoln();

    vector<int> user_idx;
    string line = ouf.readLine();
    if (!line.empty()) {
        istringstream iss(line);
        int x;
        while (iss >> x) {
            user_idx.push_back(x);
        }
    }
    vector<char> used(m + 1, 0);
    int recomputed = 0;
    for (int idx : user_idx) {
        if (idx < 1 || idx > n)
            quitf(_wa, "Permit index %d is out of range [1..%d]", idx, n);
        for (int s = permits[idx].start; s <= permits[idx].end; s++) {
            if (used[s]) {
                quitf(_wa, "Sector %d is explored by more than one expedition",
                      s);
            }
            used[s] = 1;
        }
        recomputed += permits[idx].credits;
    }
    if (recomputed != user_income) {
        quitf(_wa,
              "Your list of permits actually yields %d credits, "
              "but you claimed %d credits.",
              recomputed, user_income);
    }
    if (user_income > opt_K) {
        quitf(
            _wa,
            "Your solution (%d credits) exceeds judge’s optimal (%d credits)!",
            user_income, opt_K);
    }
    if (user_income < opt_K) {
        quitf(_wa,
              "Your solution (%d credits) is worse than optimal (%d credits).",
              user_income, opt_K);
    }

    quitf(_ok, "Correct Answer!");
}
