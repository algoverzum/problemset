// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    cin >> S;
    sort(S.begin(), S.end());
    cout << S << "\n";
}
