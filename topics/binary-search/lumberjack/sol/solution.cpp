// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

#include <iostream>
#include <vector>
using namespace std;

long long collected_wood(const vector<int> &A, int H) {
    long long total = 0;
    for (int h : A) {
        if (h > H) total += (h - H);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> A(N);
    for (int &x : A) cin >> x;

    int lo = 0;
    int hi = 1000000000;

    while (hi - lo > 1) {
        int mid = (lo + hi) / 2;
        if (collected_wood(A, mid) >= M) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    cout << lo << '\n';
    return 0;
}
