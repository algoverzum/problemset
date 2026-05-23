// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int A;
    int N;
    cin >> A >> N;

    vector<int> motes(N);
    for (int i = 0; i < N; i++) {
        cin >> motes[i];
    }

    sort(motes.begin(), motes.end());

    int ans;

    if (A == 1) {
        ans = N;
    } else {
        ans = N; // remove everything
        int ops = 0;

        for (int i = 0; i < N; i++) {
            ans = min(ans, ops + (N - i));

            while (A <= motes[i]) {
                A += A - 1;
                ops++;
            }

            A += motes[i];
        }

        ans = min(ans, ops);
    }

    cout << ans << '\n';
    return 0;
}
