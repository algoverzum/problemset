// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> good_indices;
    for (int i = 1; i <= n; i++) {
        int hands;
        cin >> hands;
        if (hands <= 4) {
            good_indices.push_back(i);
        }
    }
    cout << good_indices.size() << "\n";
    for (int index : good_indices) {
        cout << index << " ";
    }
    cout << "\n";
    return 0;
}
