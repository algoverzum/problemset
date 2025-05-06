// @check-accepted: examples
// @check-time-limit-exceeded: all
#include <iostream>
#include <vector>

using namespace std;

vector<int> coins;

bool possible(int x) {
    if (x == 0)
        return true;
    if (x < 0)
        return false;
    for (int coin : coins) {
        if (possible(x - coin))
            return true;
    }
    return false;
}

int main() {
    int n, q;
    cin >> n >> q;
    coins.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    for (int j = 0; j < q; j++) {
        int x;
        cin >> x;
        cout << (possible(x) ? "YES" : "NO") << '\n';
    }
}