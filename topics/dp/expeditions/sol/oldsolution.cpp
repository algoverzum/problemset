// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Permit {
    int start, end, credits, id;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<Permit> permits(n);
    for (int i = 0; i < n; i++) {
        cin >> permits[i].start >> permits[i].end >> permits[i].credits;
        permits[i].id = i + 1;
    }
    sort(permits.begin(), permits.end(),
         [](const Permit &a, const Permit &b) { return a.end < b.end; });
    vector<int> dp(m + 2, 0);
    vector<int> choice(m + 2, -1);
    vector<int> previous(m + 2, -1);

    int permitIndex = 0;
    for (int sector = 1; sector <= m; sector++) {
        dp[sector] = dp[sector - 1];
        previous[sector] = sector - 1;
        while (permitIndex < n && permits[permitIndex].end == sector) {
            int startSector = permits[permitIndex].start;
            int gain = dp[startSector - 1] + permits[permitIndex].credits;
            if (gain > dp[sector]) {
                dp[sector] = gain;
                choice[sector] = permits[permitIndex].id;
                previous[sector] = startSector - 1;
            }
            permitIndex++;
        }
    }

    cout << dp[m] << '\n';

    vector<int> selected;
    int current = m;
    while (current > 0) {
        if (choice[current] != -1) {
            selected.push_back(choice[current]);
            current = previous[current];
        } else {
            current--;
        }
    }

    for (int id : selected) {
        cout << id << " ";
    }
    cout << '\n';
    return 0;
}