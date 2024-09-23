// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> bonie = {1, 1};
    for (int i = 2; i <= n; i++) {
        bonie.push_back(bonie[i - 1] + bonie[i - 2]);
    }
    for (int i = 0; i <= n; i++) {
        cout << bonie[i] << " ";
    }
    cout << "\n";
    return 0;
}
