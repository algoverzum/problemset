// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using pii = pair<int, int>;

int main() {
    int n;
    cin >> n;
    int a, b;
    cin >> a >> b;
    vector<vector<int>> pours(a + 1, vector<int>(b + 1, -1));
    queue<pii> q;
    q.push({0, 0});
    pours[0][0] = 0;
    int solution = -1;
    while (!q.empty() && solution == -1) {
        auto [x, y] = q.front();
        q.pop();
        for (int i = 0; i < 6; i++) {
            int nx, ny;
            if (i == 0) {
                nx = a;
                ny = y;
            } else if (i == 1) {
                nx = x;
                ny = b;
            } else if (i == 2) {
                nx = 0;
                ny = y;
            } else if (i == 3) {
                nx = x;
                ny = 0;
            } else if (i == 4) {
                nx = x - min(x, b - y);
                ny = y + min(x, b - y);
            } else {
                nx = x + min(y, a - x);
                ny = y - min(y, a - x);
            }
            if (ny == n) {
                solution = pours[x][y] + 1;
            }
            if (pours[nx][ny] == -1) {
                pours[nx][ny] = pours[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    cout << solution << "\n";
    return 0;
}
