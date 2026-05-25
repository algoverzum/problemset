// @check-accepted: *
#include <iostream>
#include <numeric>

using namespace std;

bool is_power_of_two(long long x) { return (x & (x - 1)) == 0; }

int main() {
    long long P, Q;
    cin >> P >> Q;

    long long g = gcd(P, Q);
    P /= g;
    Q /= g;

    if (!is_power_of_two(Q)) {
        cout << "impossible\n";
        return 0;
    }

    int gen = 0;
    while (P < Q) {
        P *= 2;
        gen++;
    }

    cout << gen << '\n';
    return 0;
}
