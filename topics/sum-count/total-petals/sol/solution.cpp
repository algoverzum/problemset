// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  int inp;
  int count = 0;
  for (int i = 0; i < n; i++) {
    cin >> inp;
    if (inp % 2 == 1) {
      count += inp;
    }
  }
  cout << count << '\n';
  return 0;
}
