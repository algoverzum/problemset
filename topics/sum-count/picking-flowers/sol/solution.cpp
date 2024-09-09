// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
<<<<<<< HEAD
    int n;
    cin >> n;
    int count = 0;
    int in;
    for (int i = 0; i < n; i++) {
        cin >> in;
        if (in % 2 == 0) {
            count++;
        }
    }
    cout << count << '\n';
    return 0;
=======
    int n;
    cin >> n;
    int count = 0;
    for (int i = 0; i < n; i++) {
        int petals;
        cin >> petals;
        if (petals % 2 == 0) {
            count++;
        }
    }
    cout << count << "\n";
    return 0;
>>>>>>> 300991843902251dbdcceaeb00fc0f23adfaa6f0
}
