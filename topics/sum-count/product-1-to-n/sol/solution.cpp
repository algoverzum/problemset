// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  int prod = 1;
  for (int i = 1; i <= n; i++) {
    prod *= i;
  }
  cout << prod << "\n";
  return 0;
}
