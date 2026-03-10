#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt(); // read input
    inf.readEoln();
    vector<int> weights(N);
    for (int i = 0; i < N; ++i) {
        weights[i] = inf.readInt();
    }

    int opt_sol = ans.readInt(); // official solution, first line is enough

    // user solution:
    int user_sol = ouf.readInt();
    if (user_sol < 0)
        user_sol *= -1;
    ouf.seekEoln();
    int left = ouf.readInt();
    vector<int> left_cargo(left);
    for (int i = 0; i < left; ++i) {
        left_cargo[i] = ouf.readInt(1, N);
    }
    ouf.seekEoln();
    int right = ouf.readInt();
    vector<int> right_cargo(right);
    for (int i = 0; i < right; ++i) {
        right_cargo[i] = ouf.readInt(1, N);
    }

    // check ans first line
    if (user_sol > opt_sol) {
        quitf(
            _wa,
            "Not optimal solution: %d difference, but it can be solved with %d",
            user_sol, opt_sol);
    }
    if (user_sol < opt_sol) {
        quitf(_wa, "Too small difference OR official solution is broken.");
    }

    // Check solution
    vector<bool> used(N, true);
    int left_sum = 0;
    int right_sum = 0;
    for (int i = 0; i < left; ++i) {
        if (used[left_cargo[i] - 1]) {
            used[left_cargo[i] - 1] = false;
            left_sum += weights[left_cargo[i] - 1];
        } else {
            quitf(_wa, "Container used more than once");
        }
    }
    for (int i = 0; i < right; ++i) {
        if (used[right_cargo[i] - 1]) {
            used[right_cargo[i] - 1] = false;
            right_sum += weights[right_cargo[i] - 1];
        } else {
            quitf(_wa, "Container used more than once");
        }
    }
    if (abs(left_sum - right_sum) != user_sol) {
        quitf(_wa, "Incorrect difference");
    }
    if (left + right != N) {
        quitf(_wa, "Some of the continers were not used");
    }
    quitf(_ok, "Correct Answer");
}
