// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int k, n;
    cin >> k >> n;

    vector<tuple<int, int, int>> pilots;
    pilots.emplace_back(k, k + 1, 0);

    for (int i = 0; i < n; i++) {
        int s, e;
        cin >> s >> e;
        pilots.emplace_back(s, e, i + 1);
    }

    sort(pilots.begin(), pilots.end());

    vector<int> res;
    int reached = 0, cur_end = 0, last = -1;
    size_t i = 0;

    while (i < pilots.size()) {
        int start, end, index;
        tie(start, end, index) = pilots[i];

        if (start <= reached) {
            i++;
            if (cur_end < end) {
                last = index;
                cur_end = end;
            }
        } else {
            res.push_back(last);
            reached = cur_end;
            if (start > cur_end) {
                cout << "0\n";
                return 0;
            }
        }
    }

    cout << res.size() << "\n";
    for (int r : res) {
        cout << r << " ";
    }
    cout << "\n";

    return 0;
}
