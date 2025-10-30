// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int SA = 0;
    int SB = 0;
    for (int i = 1; i <= 3; i++) {
        SA += A % 10;
        A /= 10;
        SB += B % 10;
        B /= 10;
    }
    if (SA >= SB) {
        cout << SA << endl;
    } else {
        cout << SB << endl;
    }
}
