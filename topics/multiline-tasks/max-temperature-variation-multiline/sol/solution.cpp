// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, A, B;
    cin >> n;
    cin >> A;
    cin >> B;
    int maxdiff = B - A;
    for (int i = 0; i < n; i++) {
        cin >> A;
        cin >> B;
        maxdiff = max(maxdiff, B - A);
    }
    cout << maxdiff << "\n";
}
