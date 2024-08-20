// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  if (a % 2 == 0 && b % 2 == 0) {
    cout << 2;
  } else if (a % 2 == 0 || b % 2 == 0) {
    cout << 1;
  } else {
    cout << 0;
  }
  return 0;
}
