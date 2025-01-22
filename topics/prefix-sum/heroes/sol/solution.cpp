// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int m = 1000000;
    int n;
    cin >> n;
    vector<int> cnt(m + 2);
    for (int i = 0; i < n; i++) {
        int arr, leave;
        cin >> arr >> leave;
        cnt[arr] += 1;
        cnt[leave + 1] -= 1;
    }
    int ans = 0;
    for (int i = 1; i <= m; i++) {
        cnt[i] += cnt[i - 1];
        ans = max(ans, cnt[i]);
    }
    cout << ans << "\n";
}
