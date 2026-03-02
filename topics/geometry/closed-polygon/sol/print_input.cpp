// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

struct point {
    ll x, y, id;
};

int main() {
    int n;
    cin >> n;
    vector<point> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i].x >> p[i].y;
        p[i].id = i + 1;
    }

    for (point q : p) {
        cout << q.id << " ";
    }
    cout << "\n";
}
