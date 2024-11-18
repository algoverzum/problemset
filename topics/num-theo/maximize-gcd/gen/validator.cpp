#include "testlib.h"
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    registerValidation();
    int t = inf.readInt(1, 100, "t");
    inf.readEoln();
    for (int i = 0; i < t; i++) {
        int a = inf.readInt(1, 1'000'000'000, "a");
        inf.readSpace();
        int b = inf.readInt(1, 1'000'000'000, "b");
        inf.readSpace();
        int k = inf.readInt(1, 1'000'000'000, "k");
        inf.readEoln();
    }
    inf.readEof();
}
