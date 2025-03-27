#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    vector<int> unique_ids;
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;

        bool found = false;
        for (int y : unique_ids) {
            if (y == x) {
                found = true;
                break;
            }
        }

        if (!found)
            unique_ids.push_back(x);
    }
    for (int i = 0; i < M; ++i) {
        int x;
        cin >> x;

        bool found = false;
        for (int y : unique_ids) {
            if (y == x) {
                found = true;
                break;
            }
        }

        if (!found)
            unique_ids.push_back(x);
    }
    sort(unique_ids.begin(), unique_ids.end());
    cout << unique_ids.size() << "\n";
    for (size_t i = 0; i < unique_ids.size(); ++i) {
        if (i > 0)
            cout << " ";
        cout << unique_ids[i];
    }
    cout << "\n";

    return 0;
}
