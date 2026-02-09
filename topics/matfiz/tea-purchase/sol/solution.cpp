// @check-accepted: *

#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    string tea;
    int amount;
    int max_amount = -1;
    int max_index = -1;

    for (int i = 1; i <= N; i++) {
        cin >> tea >> amount;
        if (amount > max_amount) {
            max_amount = amount;
            max_index = i;
        }
    }

    cout << max_index << endl;

    return 0;
}
