// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> itemCodes(n);
    for (int i = 0; i < n; i++) {
        cin >> itemCodes[i];
    }
    for (int i = 0; i < n; i++) {
        bool unique = true;
        for (int j = 0; j < n; i++) {
            if (i != j && itemCodes[i] == itemCodes[j]) {
                unique = false;
            }
        }
        if (unique) {
            cout << itemCodes[i];
        }
    }
    cout << "\n";
}
