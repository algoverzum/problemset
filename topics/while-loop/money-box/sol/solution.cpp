// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int money = 0;
    int day = 0;
    while (money < n) {
        day += 1;
        money += day;
    }
    cout << day << "\n";
    return 0;
}
