// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int s = n % 60;
    n /= 60;
    int m = n % 60;
    n /= 60;
    int h = n % 24;
    n /= 24;
    int d = n;
    cout << d << " " << h << " " << m << " " << s << "\n";
    return 0;
}
