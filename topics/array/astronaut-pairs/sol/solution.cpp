// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> weights(n);

    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    int pair_count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (weights[i] == weights[j]) {
                pair_count++;
            }
        }
    }
    cout << pair_count << "\n";
}
