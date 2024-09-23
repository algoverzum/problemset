// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> t(n);
  for (int i = 0; i < n; i++) {
    cin >> t[i];
  }
  int minindex = 0;
  for (int i = 1; i < n; i++) {
    if (t[i] < t[minindex]) {
      minindex = i;
    }
  }
  cout << t[minindex] << "\n";
  cout << minindex + 1 << "\n";
  return 0;
}
