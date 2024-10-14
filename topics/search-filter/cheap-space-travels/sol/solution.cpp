// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> dist(n + 1), price(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> dist[i] >> price[i];
    }
    vector<int> cheap;
    for (int i = 1; i <= n; i++) {
        if (price[i] <= dist[i] * 100) {
            cheap.push_back(i);
        }
    }
    cout << cheap.size() << "\n";
    for (int i : cheap)
        cout << i << " ";
    cout << "\n";
}
