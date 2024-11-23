// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> children_count(n + 1, 0);
    for (int i = 0; i < k; i++) {
        int parentID, childID;
        cin >> parentID >> childID;
        children_count[parentID]++;
    }
    int maxi = 0;
    for (int i = 1; i <= n; i++) {
        if (children_count[i] > children_count[maxi]) {
            maxi = i;
        }
    }
    cout << maxi << '\n';
}
