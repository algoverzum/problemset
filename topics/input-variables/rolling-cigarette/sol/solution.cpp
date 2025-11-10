// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, hossz, csikk;
    cin >> n >> hossz >> csikk;

    cout << n + n * csikk / hossz << " " << n * csikk % hossz << "\n";
}
