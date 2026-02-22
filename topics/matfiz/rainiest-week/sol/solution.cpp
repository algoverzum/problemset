// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int legcsapadekosabb = 1; // a legcsapadékosabb hét sorszáma
    int max_osszeg = -1;      // eddigi legnagyobb heti összeg

    for (int i = 1; i <= N; i++) {
        int heti_sum = 0;
        for (int j = 0; j < 7; j++) {
            int x;
            cin >> x;
            heti_sum += x;
        }

        if (heti_sum > max_osszeg) {
            max_osszeg = heti_sum;
            legcsapadekosabb = i;
        }
    }

    cout << legcsapadekosabb << "\n";
    return 0;
}
