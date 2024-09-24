// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> t[i];
    }
    int minindex = 1;
    for (int i = 2; i <= n; i++) {
        if (t[i] < t[minindex]) {
            minindex = i;
        }
    }
    cout << t[minindex] << "\n";
    cout << minindex << "\n";
    return 0;
}
