#include "testlib.h"
#include <iostream>

using namespace std;
const int NMAX = 2e5, TMAX = 1e4, VMAX = 1e9;

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    registerValidation(argc, argv);
    int t = inf.readInt(1, TMAX, "t"), s = 0;
    inf.readEoln();
    for (int tid = 1; tid <= t; tid++) {
        setTestCase(tid);
        int n = inf.readInt(2, NMAX, "n");
        s += n;
        ensuref(s <= NMAX, "sum of n exceeds %d", NMAX);
        inf.readEoln();
        inf.readInts(n, 0, VMAX, "a");
        inf.readEoln();
        inf.readInts(n - 1, 0, VMAX, "b");
        inf.readEoln();
    }
    inf.readEof();
    return 0;
}
