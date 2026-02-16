#include <iostream>
#include <vector>
using namespace std;

long long collected_wood(const vector<long long>& A, long long H) {
    long long total = 0;
    for (long long h : A) {
        if (h > H) total += (h - H);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M;
    cin >> N >> M;

    vector<long long> A(N);
    long long maxH = 0;
    for (long long &x : A) {
        cin >> x;
        if (x > maxH) maxH = x;
    }

    long long best = 0;

    for (long long H = 0; H <= maxH; ++H) {
        if (collected_wood(A, H) >= M) {
            best = H;
        }
    }

    cout << best << '\n';
    return 0;
}
