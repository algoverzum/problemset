// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int N, K, S;
vector<int> a;

bool can(int X) {
    int trucks = 1;
    int sum = 0;

    for (int i = 0; i < X; i++) {
        if (a[i] > S)
            return false;

        if (sum + a[i] <= S) {
            sum += a[i];
        } else {
            trucks++;
            sum = a[i];
        }

        if (trucks > K)
            return false;
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K >> S;

    a.resize(N);
    for (int i = 0; i < N; i++)
        cin >> a[i];

    int lo = 0, hi = N;

    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;

        if (can(mid))
            lo = mid;
        else
            hi = mid - 1;
    }

    cout << lo << "\n";
    return 0;
}