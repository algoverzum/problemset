#define CMS
#include "testlib.h"
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    inf.readEoln();
    vector<int> values(n + 1);

    int totalsum = 0;
    for (int i = 1; i <= n; i++) {
        values[i] = inf.readInt();
        totalsum += values[i];
    }
    int opt_K = ans.readInt();
    int user_value = ouf.readInt();
    ouf.readEoln();
    vector<int> user_idx1;
    vector<int> user_idx2;

    string line1 = ouf.readLine();
    string line2 = ouf.readLine();
    if (!line1.empty()) {
        istringstream iss(line1);
        int x;
        while (iss >> x) {
            user_idx1.push_back(x);
        }
    }

    if (!line2.empty()) {
        istringstream iss(line2);
        int x;
        while (iss >> x) {
            user_idx2.push_back(x);
        }
    }

    vector<bool> used(n, false);
    int sum1 = 0;
    int sum2 = 0;
    for (int i1 : user_idx1) {
        if (i1 < 1 || i1 > n) {
            quitf(_wa, "%d index out of range: [1..n].", i1);
        }
        if (used[i1]) {
            quitf(_wa, "%d value was already in use.", i1);
        } else {
            used[i1] = true;
            totalsum -= values[i1];
            sum1 += values[i1];
        }
    }
    for (int i2 : user_idx2) {
        if (i2 < 1 || i2 > n) {
            quitf(_wa, "%d index out of range: [1..n].", i2);
        }
        if (used[i2]) {
            quitf(_wa, "%d value was already in use.", i2);
        } else {
            used[i2] = true;
            totalsum -= values[i2];
            sum2 += values[i2];
        }
    }
    if (totalsum != user_value) {
        quitf(_wa,
              " %d value remains with your list of claimed planets , "
              "but you calculated %d value.",
              totalsum, user_value);
    }
    if (sum1 != sum2) {
        quitf(_wa,
              "The 2 successors value is not equal. one of them had: %d, the "
              "other: %d",
              sum1, sum2);
    }
    if (opt_K > user_value) {
        quitf(_wa,
              "The total value of the remaining planets is not minimal. your "
              "minimal value: %d, the lowest possible minimal value: %d",
              opt_K, user_value);
    }
    if (opt_K < user_value) {
        quitf(_wa,
              "Your solution (%d value) is lower than the judge’s optimal (%d "
              "value)!",
              opt_K, user_value);
    }

    quitf(_ok, "Correct Answer!");
}
