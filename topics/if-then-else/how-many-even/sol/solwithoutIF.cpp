// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;
  cout << 2 - A % 2 - B % 2 << "\n";
  return 0;
}

