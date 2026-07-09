// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int maxindex = 0;
    int maxvalue = 0;
    for (int i = 1; i <= n; i++) {
        int price;
        cin >> price;
        if (price <= k && price > maxvalue) {
            maxindex = i;
            maxvalue = price;
        }
    }
    cout << maxindex << "\n" << maxvalue << "\n";
    return 0;
}
