// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
  int A, B, result;
  cin >> A >> B;
  if (A % 2 == 0) {result += 1;}
  if (B % 2 == 0) {result += 1;}
  cout << result << "\n";
  return 0;
}

