// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> freq(n + 1, 0);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        freq[x]++;
    }

    int answer = -1;

    for (int num = 1; num <= n; num++) {
        if (freq[num] >= 3) {
            answer = num;
            break;
        }
    }

    cout << answer << "\n";
    return 0;
}
