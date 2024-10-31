// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    for (int i = 10; i < 100; i++) {
        int A = i / 10;
        int B = i % 10;
        if (A == B - 2) {
            cout << i - 8 << "\n";
        }
    }
}