// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        vector<int> b(n), c(m);
        for (int i = 0; i < n; i++)
            cin >> b[i];
        for (int i = 0; i < m; i++)
            cin >> c[i];

        int countWays = 0;

        // Két egymásba ágyazott ciklus – brute force
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (b[i] + c[j] <= k)
                    countWays++;
            }
        }
        cout << countWays << "\n";
    }
    return 0;
}
