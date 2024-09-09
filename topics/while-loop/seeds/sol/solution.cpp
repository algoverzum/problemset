// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int n;
  int seeds = 1;
  cin >> n;
  while (seeds < n) {
    seeds *= 3;
  }
  cout << seeds << "\n";
  return 0;
}
