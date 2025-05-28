#include <climits>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int N;
vector<int> A;
ll bestLeft = LLONG_MAX;
vector<int> bestAssign; // 0 = maradék, 1 = első testvér, 2 = második testvér

void dfs(int i, ll sum1, ll sum2, ll sumLeft, vector<int> &assign) {
    if (i == N) {
        if (sum1 == sum2 && sumLeft < bestLeft) {
            bestLeft = sumLeft;
            bestAssign = assign;
        }
        return;
    }
    // 1) ajándék a maradékba
    assign[i] = 0;
    dfs(i + 1, sum1, sum2, sumLeft + A[i], assign);
    // 2) ajándék az első testvérhez
    assign[i] = 1;
    dfs(i + 1, sum1 + A[i], sum2, sumLeft, assign);
    // 3) ajándék a második testvérhez
    assign[i] = 2;
    dfs(i + 1, sum1, sum2 + A[i], sumLeft, assign);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    A.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vector<int> assign(N, 0);
    dfs(0, 0, 0, 0, assign);

    // Kiírás
    cout << bestLeft << "\n";
    // Első testvér ajándékai
    bool first = true;
    for (int i = 0; i < N; i++) {
        if (bestAssign[i] == 1) {
            if (!first)
                cout << " ";
            cout << (i + 1);
            first = false;
        }
    }
    cout << "\n";
    // Második testvér ajándékai
    first = true;
    for (int i = 0; i < N; i++) {
        if (bestAssign[i] == 2) {
            if (!first)
                cout << " ";
            cout << (i + 1);
            first = false;
        }
    }
    cout << "\n";

    return 0;
}
