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
        cin >> intervals[i].first >> intervals[i].second;
    }

    // Sort intervals by their end time (second element of the pair)
    sort(intervals.begin(), intervals.end(),
         [](const pair<int, int> &a, const pair<int, int> &b) {
             return a.second < b.second;
         });

    vector<int> photos;
    int last_photo_time = -1;

    for (const auto &interval : intervals) {
        int start = interval.first;
        int end = interval.second;

        if (last_photo_time < start) {
            last_photo_time = end - 1;
            photos.push_back(last_photo_time);
        }
    }

    cout << photos.size() << "\n";
    for (int t : photos) {
        cout << t << " ";
    }
    cout << "\n";

    return 0;
}
