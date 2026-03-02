// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

struct point {
    ll x, y, id;
};

int turn(point a, point b, point c) {
    ll s = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    return (s > 0) - (s < 0);
}

int main() {
    int n;
    cin >> n;
    vector<point> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i].x >> p[i].y;
        p[i].id = i + 1;
    }
    for (int i = 1; i < n; i++) {
        if (p[i].x < p[0].x || p[i].x == p[0].x && p[i].y < p[0].y)
            swap(p[0], p[i]);
    }
    point center = p[0];
    sort(p.begin() + 1, p.end(), [center](point a, point b) {
        int t = turn(center, a, b);
        return t > 0 || t == 0 && (a.x < b.x || a.x == b.x && a.y < b.y);
    });

    int i = n - 2;
    while (turn(p[0], p[n - 1], p[i]) == 0)
        i--;
    reverse(p.begin() + i + 1, p.end());

    for (point q : p) {
        cout << q.id << " ";
    }
    cout << "\n";
}
