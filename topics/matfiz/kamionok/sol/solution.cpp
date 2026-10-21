// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

bool jo(const vector<long long> &t, int K, long long kapacitas) {
    int kamionok = 1;
    long long aktualis = 0;
    for (long long x : t) {
        if (aktualis + x <= kapacitas) {
            aktualis += x;
        } else {
            kamionok++;
            aktualis = x;
        }
    }
    return kamionok <= K;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<long long> t(N);
    long long bal = 0;
    long long jobb = 0;

    for (int i = 0; i < N; i++) {
        cin >> t[i];

        if (t[i] > bal)
            bal = t[i];

        jobb += t[i];
    }
    while (bal < jobb) {
        long long kozep = (bal + jobb) / 2;
        if (jo(t, K, kozep))
            jobb = kozep;
        else
            bal = kozep + 1;
    }
    cout << bal << endl;
    return 0;
}