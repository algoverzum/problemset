#include <algorithm>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <vector>

using namespace std;
using ll = long long;

struct Point {
    ll x, y;
    int id;
};

// ---------------- Common Geometry ----------------

ll cross_product(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

int orient(Point a, Point b, Point c) {
    ll v = cross_product(a, b, c);
    if (v == 0)
        return 0;
    return (v > 0) ? 1 : -1;
}

bool on_seg(Point a, Point b, Point c) {
    return c.x >= min(a.x, b.x) && c.x <= max(a.x, b.x) &&
           c.y >= min(a.y, b.y) && c.y <= max(a.y, b.y);
}

bool intersect_logic(Point p1, Point q1, Point p2, Point q2) {
    int o1 = orient(p1, q1, p2);
    int o2 = orient(p1, q1, q2);
    int o3 = orient(p2, q2, p1);
    int o4 = orient(p2, q2, q1);

    if (o1 != o2 && o3 != o4)
        return true;
    if (o1 == 0 && on_seg(p1, q1, p2))
        return true;
    if (o2 == 0 && on_seg(p1, q1, q2))
        return true;
    if (o3 == 0 && on_seg(p2, q2, p1))
        return true;
    if (o4 == 0 && on_seg(p2, q2, q1))
        return true;
    return false;
}

// ---------------- Slow Checker (O(N^2)) ----------------

bool slow_check(int N, const vector<Point> &poly) {
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            // Skip adjacent edges
            if (j == i + 1 || (i == 0 && j == N - 1))
                continue;

            if (intersect_logic(poly[i], poly[(i + 1) % N], poly[j],
                                poly[(j + 1) % N]))
                return false;
        }
    }
    return true;
}

// ---------------- Fast Checker (O(N log N)) ----------------

struct Segment {
    Point p, q;
    int id;
};

vector<Segment> global_seg;
ll sweepX;

struct Cmp {
    bool operator()(int i, int j) const {
        if (i == j)
            return false;
        const Segment &a = global_seg[i], &b = global_seg[j];

        auto get_y = [&](const Segment &s, ll x) -> double {
            if (s.p.x == s.q.x)
                return (double)s.p.y;
            return s.p.y +
                   (double)(s.q.y - s.p.y) * (x - s.p.x) / (s.q.x - s.p.x);
        };

        double y1 = get_y(a, sweepX);
        double y2 = get_y(b, sweepX);
        if (abs(y1 - y2) > 1e-9)
            return y1 < y2;
        return i < j;
    }
};

bool fast_check(int N, const vector<Point> &poly) {
    global_seg.clear();
    for (int i = 0; i < N; i++) {
        Segment s = {poly[i], poly[(i + 1) % N], i};
        if (s.q.x < s.p.x)
            swap(s.p, s.q);
        global_seg.push_back(s);
    }

    struct Event {
        ll x;
        int id;
        bool left;
        bool operator<(const Event &other) const {
            if (x != other.x)
                return x < other.x;
            return left > other.left;
        }
    };

    vector<Event> events;
    for (int i = 0; i < N; i++) {
        events.push_back({global_seg[i].p.x, i, true});
        events.push_back({global_seg[i].q.x, i, false});
    }
    sort(events.begin(), events.end());

    set<int, Cmp> active;
    for (auto &e : events) {
        sweepX = e.x;
        if (e.left) {
            auto it = active.insert(e.id).first;
            auto nxt = next(it),
                 prv = (it == active.begin() ? active.end() : prev(it));

            if (nxt != active.end()) {
                int i1 = e.id, i2 = *nxt;
                if (!(abs(i1 - i2) == 1 || abs(i1 - i2) == N - 1))
                    if (intersect_logic(global_seg[i1].p, global_seg[i1].q,
                                        global_seg[i2].p, global_seg[i2].q))
                        return false;
            }
            if (prv != active.end()) {
                int i1 = e.id, i2 = *prv;
                if (!(abs(i1 - i2) == 1 || abs(i1 - i2) == N - 1))
                    if (intersect_logic(global_seg[i1].p, global_seg[i1].q,
                                        global_seg[i2].p, global_seg[i2].q))
                        return false;
            }
        } else {
            auto it = active.find(e.id);
            if (it != active.end()) {
                auto nxt = next(it),
                     prv = (it == active.begin() ? active.end() : prev(it));
                if (nxt != active.end() && prv != active.end()) {
                    int i1 = *prv, i2 = *nxt;
                    if (!(abs(i1 - i2) == 1 || abs(i1 - i2) == N - 1))
                        if (intersect_logic(global_seg[i1].p, global_seg[i1].q,
                                            global_seg[i2].p, global_seg[i2].q))
                            return false;
                }
                active.erase(it);
            }
        }
    }
    return true;
}

// ---------------- Generator & Stress Test ----------------

int main() {
    mt19937 rng(1337);
    int tests = 10000;

    for (int t = 1; t <= tests; t++) {
        int N = uniform_int_distribution<int>(3, 20)(rng);
        vector<Point> pts(N);
        for (int i = 0; i < N; i++) {
            pts[i] = {(ll)uniform_int_distribution<int>(-20, 20)(rng),
                      (ll)uniform_int_distribution<int>(-20, 20)(rng), i};
        }

        // 50% chance to make it a simple polygon via radial sort
        if (uniform_int_distribution<int>(0, 1)(rng)) {
            ll midX = 0, midY = 0;
            for (auto p : pts) {
                midX += p.x;
                midY += p.y;
            }
            midX /= N;
            midY /= N;
            sort(pts.begin(), pts.end(), [&](Point a, Point b) {
                return atan2(a.y - midY, a.x - midX) <
                       atan2(b.y - midY, b.x - midX);
            });
        } else {
            shuffle(pts.begin(), pts.end(), rng);
        }

        bool res_slow = slow_check(N, pts);
        bool res_fast = fast_check(N, pts);

        if (res_slow != res_fast) {
            cout << "Mismatch found in test " << t << "!" << endl;
            cout << "Slow: " << (res_slow ? "Simple" : "Intersecting") << endl;
            cout << "Fast: " << (res_fast ? "Simple" : "Intersecting") << endl;
            cout << N << endl;
            for (auto p : pts)
                cout << p.x << " " << p.y << endl;
            return 0;
        }
        if (t % 1000 == 0)
            cout << "Passed " << t << " tests..." << endl;
    }

    cout << "All stress tests passed!" << endl;
    return 0;
}