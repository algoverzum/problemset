// @check-accepted: *
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int k, n;
    cin >> k >> n;

    vector<array<int, 3>> pilots;

    for (int i = 0; i < n; i++) {
        int s, e;
        cin >> s >> e;
        pilots.push_back({s, e, i + 1});
    }
    pilots.push_back({k, k + 1, -1});
    sort(pilots.begin(), pilots.end());

    vector<int> ans;
    int reached = 0, best = 0, best_end = 0;

    for (auto [start, end, index] : pilots) {
        if (start <= reached) {
            if (end > best_end) {
                best_end = end;
                best = index;
            }
        } else {
            if (start > best_end) {
                cout << "0\n";
                return 0;
            }
            reached = best_end;
            ans.push_back(best);
            best_end = end;
            best = index;
        }
    }

    cout << ans.size() << "\n";
    for (int r : ans) {
        cout << r << " ";
    }
    cout << "\n";

    return 0;
}
