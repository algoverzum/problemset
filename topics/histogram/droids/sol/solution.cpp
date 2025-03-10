// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    int szam;
    vector<int> szamok(11);
    for (int i = 0; i < n; i++) {
        cin >> szam;
        szamok[szam]++;
    }
    int maxdb = 0;
    for (int i = 1; i < 11; i++) {
        maxdb = max(maxdb, szamok[i]);
    }
    cout << maxdb << "\n";
}
