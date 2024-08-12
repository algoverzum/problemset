// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int sh, sm, eh, em;
  cin >> sh >> sm >> eh >> em;
  cout << 60 * eh + em - 60 * sh - sm << "\n";
  return 0;
}
