// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, mint;
    cin >> n;
    cin >> mint;
    int minindex = 1;
    for (int i = 2; i <= n; i++) {
        int curtemp;
        cin >> curtemp;
        if (curtemp < mint) {
            minindex = i;
            mint = curtemp;
        }
    }
    cout << mint << "\n";
    cout << minindex << "\n";
    return 0;
}
