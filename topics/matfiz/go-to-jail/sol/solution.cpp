// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    string ans = "No";
    vector<int> elso(N), masodik(N);

    for (int i = 0; i < N; i++) {
        cin >> elso[i] >> masodik[i];
    }

    for (int i = 2; i < N; i++) {
        if (elso[i] == masodik[i] && elso[i - 1] == masodik[i - 1] &&
            elso[i - 2] == masodik[i - 2]) {
            ans = "Yes";
        }
    }

    cout << ans << endl;
    return 0;
}
