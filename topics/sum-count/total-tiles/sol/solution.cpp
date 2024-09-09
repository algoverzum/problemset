// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int area = 0;
    int side;
    for (int i = 0; i < n; i++) {
        cin >> side;
        area += side * side;
    }
    cout << area << "\n";
    return 0;
}
