// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    long long K;
    cin >> N >> K;

    vector<long long> M(N);
    for (int i = 0; i < N; i++) {
        cin >> M[i];
    }

    vector<long long> diffs;
    long long hi = 0;

    for (int i = 0; i < N - 1; i++) {
        long long d = M[i + 1] - M[i];
        diffs.push_back(d);
        hi = max(hi, d);
    }

    long long lo = 0;

    while (hi - lo > 1) {
        long long mid = (lo + hi) / 2;

        long long needed = 0;
        for (long long d : diffs) {
            needed += (d - 1) / mid;
        }

        if (needed <= K) {
            hi = mid;
        } else {
            lo = mid;
        }
    }

    cout << hi << '\n';

    return 0;
}
