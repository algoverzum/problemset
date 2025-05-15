// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> mountain(0);
vector<vector<int>> memo(0);

int Rec(int i, int j) {
    if (memo[i][j] != -1) {
        return memo[i][j];
    } else {
        int height = mountain[i][j];
        int ret = 0;
        if (mountain[i + 1][j] == height + 1) {
            ret = max(ret, Rec(i + 1, j) + 1);
        }
        if (mountain[i - 1][j] == height + 1) {
            ret = max(ret, Rec(i - 1, j) + 1);
        }
        if (mountain[i][j + 1] == height + 1) {
            ret = max(ret, Rec(i, j + 1) + 1);
        }
        if (mountain[i][j - 1] == height + 1) {
            ret = max(ret, Rec(i, j - 1) + 1);
        }
        memo[i][j] = ret;
        return ret;
    }
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
            Rec(i, j);
        }
    }
    int maxlength = -1;
    int maxi = -1;
    int maxj = -1;
    for (int i = 1; i < n + 1; i++) {
        if (maxlength < memo[i][1]) {
            maxlength = memo[i][1];
            maxi = i;
            maxj = 1;
        }
    }
    for (int i = 1; i < n + 1; i++) {
        if (maxlength < memo[i][n]) {
            maxlength = memo[i][n];
            maxi = i;
            maxj = n;
        }
    }
    for (int i = 1; i < n + 1; i++) {
        if (maxlength < memo[1][i]) {
            maxlength = memo[1][i];
            maxi = 1;
            maxj = i;
        }
    }
    for (int i = 1; i < n + 1; i++) {
        if (maxlength < memo[n][i]) {
            maxlength = memo[n][i];
            maxi = n;
            maxj = i;
        }
    }
    cout << maxlength << "\n";
    cout << maxi << " " << maxj << "\n";
}