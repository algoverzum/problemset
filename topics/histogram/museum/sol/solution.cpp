// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> days(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int f, l;
        cin >> f >> l;
        for (int j = f; j <= l; j++) {
            days[j] += 1;
        }
    }
    int longest = 0;
    int last_at_least_two = 0;
    int start = 0;
    int end = 0;
    for (int i = 1; i < n + 1; i++) {
        if (days[i] >= 2) {
            last_at_least_two = i;
        } else {
            if (i - last_at_least_two > longest) {
                longest = i - last_at_least_two;
                start = 1 + last_at_least_two;
                end = i;
            }
        }
    }
    if (longest > 0) {
        cout << start << ' ' << end << "\n";
    } else {
        cout << 0 << "\n";
    }
}
