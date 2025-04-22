#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt();
    inf.readEoln();
    vector<int> orders(N + 1);
    for (int i = 1; i <= N; ++i) {
        orders[i] = inf.readInt();
    }
    int opt_K = ans.readInt();
    int user_K = ouf.readInt();
    ouf.readEoln();

    vector<int> user_pos(user_K);
    int last = -1;
    int day = 0;
    for (int i = 0; i < user_K; ++i) {
        user_pos[i] = ouf.readInt(1, N);
        if (user_pos[i] < last) {
            quitf(_wa, "Indices not in increasing order");
        }
        day++;
        if (orders[user_pos[i]] < day) {
            quitf(_wa, "The (%d). deadline has already passed.", user_pos[i]);
        }
        last = user_pos[i];
    }

    // Optimalitás
    if (user_K < opt_K) {
        quitf(_wa,
              "Not optimal solution: %d jobs done, but %d "
              "jobs could have been done.",
              user_K, opt_K);
    }
    if (user_K > opt_K) {
        quitf(_wa, "Too good to be real OR Official solution broken.");
    }

    quitf(_ok, "Correct Answer");
}
