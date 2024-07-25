// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int d,h,m,s;
    s = n % 60;
    n = n / 60;
    m = n % 60;
    n = n / 60;
    h = n % 24;
    n = n / 24;
    d = n;
    cout << d << ' ' << h << ' ' << m << ' ' << s << ' ' << "\n";
    return 0;
}
