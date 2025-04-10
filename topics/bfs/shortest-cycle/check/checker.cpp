#define CMS
#include "set"
#include "string"
#include "testlib.h"
#include "vector"
using namespace std;

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);

    int goodans = ans.readInt();
    int userans = ouf.readInt();

    if (goodans != userans)
        quitf(_wa, "wrong");

    if (userans == -1) {
        quit(_ok, "ok");
    }
    ouf.readEoln();

    int n = inf.readInt();
    int m = inf.readInt();
    int p = inf.readInt();
    set<pair<int, int>> edges;
    set<pair<int, int>> path_edges;
    for (int i = 0; i < m; i++) {
        int a = inf.readInt();
        int b = inf.readInt();
        edges.insert({min(a, b), max(a, b)});
    }

    bool rootin = false;
    int node, firstnode;
    int lastnode = -1;
    for (int i = 0; i < goodans; i++) {
        node = ouf.readInt();
        if (i == 0) {
            firstnode = node;
        }

        if (node == p) {
            if (rootin) {
                quitp(0.5, "wrong path p in path twice");
            } else {
                rootin = true;
            }
        }
        if (node < 1 || node > n) {
            quitp(0.5, "node not in graph");
        }
        if (lastnode != -1) {
            pair<int, int> edge = {min(node, lastnode), max(node, lastnode)};
            if (edges.count(edge) == 0) {
                quitp(0.5, "edge not in graph");
            }
            if (path_edges.count(edge) > 0) {
                quitp(0.5, "edge used more than once");
            }
            path_edges.insert(edge);
        }
        lastnode = node;
    }
    if (edges.count({min(node, firstnode), max(node, firstnode)}) == 0) {
        quitp(0.5, "edge not in graph");
    }
    if (path_edges.count({min(node, firstnode), max(node, firstnode)}) > 0) {
        quitp(0.5, "edge used more than once");
    }

    if (rootin) {
        quitf(_ok, "ok");
    } else {
        quitp(0.5, "wrong path p not in path");
    }
    return 0;
}
