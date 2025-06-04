// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> mountain;
vector<vector<int>> memo;
vector<pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int rec(int i, int j) {
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    int height = mountain[i][j];
    int ret = 0;
    for (auto [di, dj] : moves) {
        if (mountain[i + di][j + dj] == height + 1) {
            ret = max(ret, rec(i + di, j + dj) + 1);
        }
    }
    return memo[i][j] = ret;
}

int main() {
    int n;
    cin >> n;
    mountain.assign(n + 2, vector<int>(n + 2, -1));
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            cin >> mountain[i][j];
        }
    }
    memo.assign(n + 2, vector<int>(n + 2, -1));
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            rec(i, j);
        }
    }
    int maxlength = -1;
    int maxi = -1;
    int maxj = -1;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            if (i == 1 || i == n || j == 1 || j == n)
                if (maxlength < memo[i][j]) {
                    maxlength = memo[i][j];
                    maxi = i;
                    maxj = j;
                }
        }
    }
    cout << maxlength << "\n";
    cout << maxi << " " << maxj << "\n";
}
