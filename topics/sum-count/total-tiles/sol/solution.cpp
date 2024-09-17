// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int area = 0;
    for (int i = 0; i < n; i++) {
        int side;
        cin >> side;
        area += side * side;
    }
    cout << area << "\n";
    return 0;
}
