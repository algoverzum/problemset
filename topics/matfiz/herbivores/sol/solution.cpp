// @check-accepted: *
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<vector<string>> data(N, vector<string>(2));
  set<string> eaters;
  for (int i = 0; i < N; i++) {
    cin >> data[i][0] >> data[i][1];
    eaters.insert(data[i][0]);
  }
  // Kezdetben minden evő állat potenciálisan csak növényevő
  set<string> only_plants = eaters;

  for (int i = 0; i < N; i++) {
    // Ha állatot eszik, akkor kiesik
    if (eaters.count(data[i][1])) {
      only_plants.erase(data[i][0]);
    }
  }
  cout << only_plants.size() << endl;
  for (const auto &animal : only_plants) {
    cout << animal << endl;
  }

  return 0;
}
