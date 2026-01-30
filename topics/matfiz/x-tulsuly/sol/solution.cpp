// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int x = 0;
    for (char c : s) {
        if (c == 'x')
            x++;
    }

    int n = s.size();
    int result = min(n, 2 * x - 1);
    cout << result << '\n';

    return 0;
}
