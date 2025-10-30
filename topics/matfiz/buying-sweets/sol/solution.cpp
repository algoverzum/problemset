// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int X, A, B;
    cin >> X >> A >> B;
    // a torta vásárlás után M forint marad
    int M = X - A;
    int fank = 0;
    for (int i = M; i >= 0; i -= B) {
        fank++;
    }
    cout << M - (fank - 1) * B << endl;
}
