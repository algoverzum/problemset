// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

class FenwickTree {
    vector<int> bit;
    int n;

  public:
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int idx, int delta) {
        while (idx <= n) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }

    int query(int idx) const {
        int sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx -= idx & -idx;
        }
        return sum;
    }

    int query(int left, int right) const {
        return query(right) - query(left - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        FenwickTree ft(1000000);

        long long inversions = 0;

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;

            inversions += ft.query(1000000) - ft.query(x);
            ft.update(x, 1);
        }

        cout << inversions << '\n';
    }

    return 0;
}
