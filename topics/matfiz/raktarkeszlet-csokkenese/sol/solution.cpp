// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int sz, ered, N;
    cin >> sz >> ered >> N;
    while (sz > 0 && ered > N) {
        sz--;
        ered -= 2;
        cout << sz << "\n";
    }
    return 0;
}
