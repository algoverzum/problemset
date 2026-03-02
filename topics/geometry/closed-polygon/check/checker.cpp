#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

struct point {
    ll x, y, id;
};

int orientation(const point &a, const point &b, const point &c) {
    long long cross = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);

    if (cross == 0)
        return 0;                // collinear
    return (cross > 0) ? 1 : -1; // 1 = ccw, -1 = cw
}

bool onSegment(const point &a, const point &b, const point &c) {
    return min(a.x, b.x) <= c.x && c.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= c.y && c.y <= max(a.y, b.y);
}

bool segmentsIntersect(const point &p1, const point &q1, const point &p2,
                       const point &q2) {

    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    // General case
    if (o1 != o2 && o3 != o4)
        return true;

    // Special collinear cases
    if (o1 == 0 && onSegment(p1, q1, p2))
        return true;
    if (o2 == 0 && onSegment(p1, q1, q2))
        return true;
    if (o3 == 0 && onSegment(p2, q2, p1))
        return true;
    if (o4 == 0 && onSegment(p2, q2, q1))
        return true;

    return false;
}

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt(3, 100000);
    inf.readEoln();
    vector<point> P(N);
    for (int i = 0; i < N; i++) {
        int X = inf.readInt();
        int Y = inf.readInt();
        inf.readEoln();
        P[i].x = X;
        P[i].y = Y;
    }

    vector<int> sol(N);
    vector<int> test(N);
    for (int i = 0; i < N; i++) {
        test[i] = ouf.readInt(1, N);
        sol[i] = test[i] - 1; // index
    }

    // test permutation
    sort(test.begin(), test.end());
    for (int i = 0; i < N; i++) {
        if (test[i] != i + 1) {
            quitf(_wa, "Point %d is not on the list.", i + 1);
        }
    }

    for (int i = 0; i < N; i++) {
        point a1 = P[sol[i]];
        point a2 = P[sol[(i + 1) % N]];

        for (int j = i + 1; j < N; j++) {

            // Skip adjacent edges
            if (sol[(i + 1) % N] == sol[j])
                continue;
            if (sol[i] == sol[(j + 1) % N])
                continue;

            point b1 = P[sol[j]];
            point b2 = P[sol[(j + 1) % N]];

            if (segmentsIntersect(a1, a2, b1, b2))
                quitf(_wa, "Intersecting segments found.");
        }
    }

    quitf(_ok, "Correct solution.");
}
