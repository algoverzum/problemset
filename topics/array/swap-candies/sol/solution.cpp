// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> candies(n);
    for (int i = 0; i < n; i++) {
        cin >> candies[i];
    }
    for (int i = 0; i + 1 < candies.size(); i += 2) {
        // swap(candies[i], candies[i + 1]);
        int b = candies[i];
        candies[i] = candies[i + 1];
        candies[i + 1] = b;
    }
    for (int i = 0; i < n; i++) {
        cout << candies[i] << " ";
    }
    cout << "\n";
}
