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
    int reached = 0, curend = 0, last = -1;
    size_t i = 0;

    while (i < pilots.size()) {
        int start, end, index;
        tie(start, end, index) = pilots[i];

        if (start <= reached) {
            i++;
            if (curend < end) {
                last = index;
                curend = end;
            }
        } else {
            res.push_back(last);
            reached = curend;
            if (start > curend) {
                cout << "0\n";
                return 0;
            }
        }
    }

    cout << res.size() << endl;
    for (int r : res) {
        cout << r << " ";
    }
    cout << "\n";

    return 0;
}
