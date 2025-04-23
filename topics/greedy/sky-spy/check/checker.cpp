#define CMS
#include "testlib.h"
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt(); // read input
    inf.readEoln();
    vector<pair<int, int>> intervals(N);
    for (int i = 0; i < N; ++i) {
        intervals[i].first = inf.readInt();
        intervals[i].second = inf.readInt();
    }

    int opt_sol = ans.readInt(); // official solution, first line is enough

    // user solution:
    int user_sol = ouf.readInt();
    ouf.readEoln();
    vector<int> user_photos(user_sol);
    for (int i = 0; i < user_sol; ++i) {
        user_photos[i] = ouf.readInt();
    }

    // check ans first line
    if (user_sol > opt_sol) {
        quitf(_wa,
              "Not optimal solution: %d pictures, but it can be solved with %d",
              user_sol, opt_sol);
    }
    if (user_sol < opt_sol) {
        quitf(_wa, "Too few pictures OR Official solution broken.");
    }

    // Check solution
    sort(user_photos.begin(), user_photos.end());
    sort(intervals.begin(), intervals.end(),
         [](const pair<int, int> &a, const pair<int, int> &b) {
             return a.first < b.first;
         });

    int i = 0; // pointer for user_photos

    for (const auto &interval : intervals) {
        int start = interval.first;
        int end = interval.second;

        // Move pointer until we reach a photo within or beyond the interval
        while (i < user_sol && user_photos[i] < start) {
            ++i;
        }

        // If there's no photo in the current interval, return false
        if (i >= user_sol || user_photos[i] >= end) {
            quitf(_wa, "Some of the intervalls is not pinned");
        }
    }

    quitf(_ok, "Correct Answer");
}
