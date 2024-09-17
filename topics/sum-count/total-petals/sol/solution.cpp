// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int petals;
        cin >> petals;
        if (petals % 2 == 1) {
            sum += petals;
        }
    }
    cout << sum << "\n";
    return 0;
}
