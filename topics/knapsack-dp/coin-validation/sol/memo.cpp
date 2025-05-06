// @check-accepted: *
#include <iostream>
#include <vector>

using namespace std;

const int MAX_X = 1000000;

vector<int> coins;
vector<int> memo(MAX_X + 1, -1);

bool possible(int x) {
    if (x == 0)
        return true;
    if (x < 0)
        return false;
    if (memo[x] != -1)
        return memo[x];
    bool result = false;
    for (int coin : coins) {
        if (possible(x - coin))
            result = true;
    }
    memo[x] = result;
    return result;
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