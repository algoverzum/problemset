// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;
    int in;
    for (int i = 0; i < n; i++) {
        cin >> in;
        if (in % 2 == 0) {
            count++;
        }
    }
    cout << count << '\n';
    return 0;
}
