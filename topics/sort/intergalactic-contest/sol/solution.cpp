// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<tuple<int, int, int>> v;
    for (int i = 1; i <= n; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b, i});
    }
    sort(v.begin(), v.end(),
         [](const tuple<int, int, int> &a, const tuple<int, int, int> &b) {
             if (get<0>(a) != get<0>(b))
                 return get<0>(a) > get<0>(b);
             return get<1>(a) < get<1>(b);
         });
    for (const auto &[a, b, index] : v) {
        cout << index << " ";
    }
    cout << "\n";
    return 0;
}
