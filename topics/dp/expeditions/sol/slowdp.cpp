// @check-accepted: *
// elvileg ez sem kéne, hogy időlimites legyen, nem?

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Permit {
    int start, end, credits;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<Permit> permits(n);
    for (int i = 0; i < n; i++) {
        cin >> permits[i].start >> permits[i].end >> permits[i].credits;
    }

    vector<int> dp(m + 2, 0);
    vector<int> choice(m + 2, -1);
    vector<int> previous(m + 2, -1);

    for (int sector = 1; sector <= m; sector++) {
        dp[sector] = dp[sector - 1];
        previous[sector] = sector - 1;
        for (int permitIndex = 0; permitIndex < n; permitIndex++) {
            if (permits[permitIndex].end == sector) {
                int startSector = permits[permitIndex].start;
                int gain = dp[startSector - 1] + permits[permitIndex].credits;
                if (gain > dp[sector]) {
                    dp[sector] = gain;
                    choice[sector] = permitIndex;
                    previous[sector] = startSector - 1;
                }
            }
        }
    }

    cout << dp[m] << '\n';

    vector<int> selected;
    int current = m;
    while (current > 0) {
        if (choice[current] != -1) {
            selected.push_back(choice[current] + 1);
            current = previous[current];
        } else {
            current--;
        }
    }
    sort(selected.begin(), selected.end());
    for (int id : selected) {
        cout << id << " ";
    }
    cout << '\n';
    return 0;
}