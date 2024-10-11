// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int days = 0;
    int currentday;
    cin >> currentday;
    while (currentday != 0) {
        cin >> currentday;
        days += 1;
    }
    cout << days << "\n";
    return 0;
}
