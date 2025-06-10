// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> intervals(N);
    for (int i = 0; i < N; ++i) {
        // The first is the departure because we want to sort them according to
        // that.
        cin >> intervals[i].second >> intervals[i].first;
    }

    sort(intervals.begin(), intervals.end());

    vector<int> photos;
    int last_photo = -1;

    for (auto [end, start] : intervals) {
        if (last_photo < start) {
            last_photo = end - 1;
            photos.push_back(last_photo);
        }
    }

    cout << photos.size() << "\n";
    for (int t : photos) {
        cout << t << " ";
    }
    cout << "\n";

    return 0;
}
