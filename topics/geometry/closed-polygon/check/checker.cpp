#define CMS
#include "testlib.h"
#include <algorithm>
#include <set>
#include <vector>
using namespace std;
using ll = long long;

struct Point {
    ll x, y;
};
struct Segment {
    Point p, q;
    int id;
};

int N;
vector<Segment> seg;
ll sweepX;

// ---------------- Geometry ----------------
ll cross(const Point &a, const Point &b, const Point &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

int orient(const Point &a, const Point &b, const Point &c) {
    ll v = cross(a, b, c);
    if (v == 0)
        return 0;
    return (v > 0) ? 1 : -1;
}

bool onSeg(const Point &a, const Point &b, const Point &c) {
    return min(a.x, b.x) <= c.x && c.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= c.y && c.y <= max(a.y, b.y);
}

bool intersect(const Segment &s1, const Segment &s2) {
    const Point &p1 = s1.p, &q1 = s1.q, &p2 = s2.p, &q2 = s2.q;
    int o1 = orient(p1, q1, p2);
    int o2 = orient(p1, q1, q2);
    int o3 = orient(p2, q2, p1);
    int o4 = orient(p2, q2, q1);

    if (o1 != o2 && o3 != o4)
        return true;
    if (o1 == 0 && onSeg(p1, q1, p2))
        return true;
    if (o2 == 0 && onSeg(p1, q1, q2))
        return true;
    if (o3 == 0 && onSeg(p2, q2, p1))
        return true;
    if (o4 == 0 && onSeg(p2, q2, q1))
        return true;
    return false;
}

// ---------------- Sweep comparator ----------------
struct Cmp {
    bool operator()(int i, int j) const {
        if (i == j)
            return false;
        const Segment &a = seg[i], &b = seg[j];
        ll x = sweepX;

        Point pa = (a.p.x <= x) ? a.p : a.q;
        Point qa = (a.p.x > x) ? a.p : a.q;
        Point pb = (b.p.x <= x) ? b.p : b.q;

        int o = orient(pa, qa, pb);
        if (o != 0)
            return o < 0;
        return i < j;
    }
};

// ---------------- Point equality ----------------
bool same(const Point &a, const Point &b) { return a.x == b.x && a.y == b.y; }

// ---------------- Adjacent edge backtracking check ----------------
bool adjacent_overlap(const Segment &s1, const Segment &s2) {
    if (orient(s1.p, s1.q, s2.p) != 0 || orient(s1.p, s1.q, s2.q) != 0)
        return false;

    auto cmp = [](const Point &a, const Point &b) {
        if (a.x != b.x)
            return a.x < b.x;
        return a.y < b.y;
    };

    vector<Point> pts = {s1.p, s1.q, s2.p, s2.q};
    sort(pts.begin(), pts.end(), cmp);

    bool s1_has_middle = same(pts[1], s1.p) || same(pts[1], s1.q);
    bool s2_has_middle = same(pts[2], s1.p) || same(pts[2], s1.q);

    return !(s1_has_middle &&
             s2_has_middle); // overlapping interiors → backtracking
}

// ---------------- Check overlap ----------------
bool check_overlap(const Segment &s1, const Segment &s2) {
    // adjacent edges
    if (abs(s1.id - s2.id) == 1 || abs(s1.id - s2.id) == N - 1) {
        return adjacent_overlap(s1, s2);
    }
    // non-adjacent edges
    return intersect(s1, s2);
}

// ---------------- Polygon validator ----------------
bool validatePolygon(const vector<Point> &P) {
    N = P.size();
    seg.clear();
    for (int i = 0; i < N; i++) {
        Segment s;
        s.p = P[i];
        s.q = P[(i + 1) % N];
        s.id = i;
        if (s.q.x < s.p.x)
            swap(s.p, s.q);
        seg.push_back(s);
    }

    struct Event {
        ll x;
        int id;
        bool left;
    };
    vector<Event> events;
    for (int i = 0; i < N; i++) {
        events.push_back({seg[i].p.x, i, true});
        events.push_back({seg[i].q.x, i, false});
    }
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x)
            return a.x < b.x;
        return a.left > b.left;
    });

    set<int, Cmp> active;
    for (auto &e : events) {
        sweepX = e.x;
        int id = e.id;

        if (e.left) {
            auto it = active.insert(id).first;
            auto pit = (it == active.begin() ? active.end() : prev(it));
            auto nit = next(it);

            if (pit != active.end() && check_overlap(seg[*pit], seg[id]))
                return false;
            if (nit != active.end() && check_overlap(seg[*nit], seg[id]))
                return false;

        } else {
            auto it = active.find(id);
            if (it == active.end())
                continue;
            auto pit = (it == active.begin() ? active.end() : prev(it));
            auto nit = next(it);

            if (pit != active.end() && nit != active.end() &&
                check_overlap(seg[*pit], seg[*nit]))
                return false;

            active.erase(it);
        }
    }
    return true;
}

// ---------------- Main ----------------
int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    N = inf.readInt(3, 100000);
    vector<Point> P(N);
    for (int i = 0; i < N; i++) {
        int X = inf.readInt();
        int Y = inf.readInt();
        P[i].x = X;
        P[i].y = Y;
        if (i != N - 1)
            inf.readEoln();
    }

    vector<int> test(N);
    vector<int> sol(N);
    for (int i = 0; i < N; i++) {
        test[i] = ouf.readInt(1, N);
        sol[i] = test[i] - 1;
    }

    vector<int> tmp = test;
    sort(tmp.begin(), tmp.end());
    for (int i = 0; i < N; i++)
        if (tmp[i] != i + 1)
            quitf(_wa, "Point %d missing", i + 1);

    vector<Point> polygon(N);
    for (int i = 0; i < N; i++)
        polygon[i] = P[sol[i]];

    if (!validatePolygon(polygon))
        quitf(_wa, "Crossing or backtracking detected");

    quitf(_ok, "Correct solution");
}
