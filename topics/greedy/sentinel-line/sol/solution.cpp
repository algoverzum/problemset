// @check-accepted: *

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, H;
    cin >> N >> H;

    vector<int> stations(N);
    for (int i = 0; i < N; ++i) {
        cin >> stations[i];
    }

    vector<int> generators;
    int i = 0;
    while (i < N) {
        int start = stations[i];

        while (i < N && stations[i] <= start + H) {
            ++i;
        }

        int center = stations[i - 1];
        generators.push_back(i);

        while (i < N && stations[i] <= center + H) {
            ++i;
        }
    }

    cout << generators.size() << endl;
    for (int pos : generators) {
        cout << pos << " ";
    }
    cout << "\n";

    return 0;
}
