// @check-accepted: *
#include <iostream>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;

    stack<int> s;
    int akt = 1;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        while (akt <= n && (s.empty() || s.top() != x)) {
            s.push(akt++);
        }

        if (!s.empty() && s.top() == x) {
            s.pop();
        } else {
            cout << "NEM" << endl;
            return 0;
        }
    }

    cout << "IGEN" << endl;
    return 0;
}
