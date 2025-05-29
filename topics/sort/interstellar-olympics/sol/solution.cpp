// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

bool Compare(tuple<int, int, int, int> a, tuple<int, int, int, int> b) {
    if (get<0>(a) != get<0>(b)) {
        return get<0>(a) > get<0>(b);
    } else if (get<1>(a) != get<1>(b)) {
        return get<1>(a) > get<1>(b);
    } else if (get<2>(a) != get<2>(b)) {
        return get<2>(a) > get<2>(b);
    } else {
        return get<3>(a) < get<3>(b);
    }
}

int main() {
    int n;
    cin >> n;
    vector<tuple<int, int, int, int>> medals(n);
    for (int i = 0; i < n; i++) {
        int g, s, b;
        cin >> g >> s >> b;
        medals[i] = make_tuple(g, s, b, i + 1);
    }
    sort(medals.begin(), medals.end(), Compare);
    for (int i = 0; i < n; i++) {
        cout << get<3>(medals[i]) << " ";
    }
    cout << "\n";
}
