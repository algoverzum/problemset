#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>

using namespace std;
struct Permit {
    int start, end, credits;
};

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt();
    int M = inf.readInt();
    inf.readEoln();
    vector<Permit> permits(n + 2);
    for (int i = 1; i <= n; i++) {
        cin >> permits[i].start >> permits[i].end >> permits[i].credits;
    }

    // Hivatalos megoldásból csak az első sor kell
    int opt_K = ans.readInt();
    // ans.readEoln();
    // vector<int> opt_pos(opt_K);
    // for (int i = 0; i < opt_K; ++i) {
    //   opt_pos[i] = ans.readInt(1, N);
    // }

    // Versenyző megoldása
    int user_K = ouf.readInt();
    ouf.readEoln();
    vector<int> user_pos(user_K);
    int last = 0;
    for (int i = 0; i < user_K; ++i) {
        user_pos[i] = ouf.readInt(1, N);
        if (user_pos[i] <= last) {
            quitf(_wa, "Answers are not in increasing order!");
        }
        last = user_pos[i];
    }
    vector<int> cells(m + 1, 0);
    int income = 0;
    for (int exp : user_pos) {
        for (int i = permits[exp].start; i <= permits[exp].end; i++) {
            if (cells[i] == 1) {
                quitf(_wa, "Someone already worked on the cell number %d ", i);
            }
            cells[i] = 1;
        }
        income += permits[exp].credits;
    }
    if (income != User_K) {
        quitf(_wa, "The income from the list of expeditions you gave does not "
                   "match the income you gave.");
    }
    if (user_K > opt_K) {
        quitf(_wa,
              "Solution is not optimal. your income: %d, best possible income: "
              " %d ",
              user_K, opt_K);
    }
    if (user_K < opt_K) {
        quitf(_wa,
              "Either offical solution broken or your answer is too high.");
    }

    quitf(_ok, "Correct Answer!");
}
