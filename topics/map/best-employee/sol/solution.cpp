// @check-accepted: *
#include <iostream>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<int, int> ID_to_time;
    int max_time = 0, max_ID = 0;

    for (int i = 0; i < n; i++) {
        int ID, type, time;
        cin >> ID >> type >> time;
        if (type == 1) {
            ID_to_time[ID] = time;
        } else {
            int diff = time - ID_to_time[ID];
            if (diff > max_time) {
                max_time = diff;
                max_ID = ID;
            }
        }
    }
    cout << max_ID << ' ' << max_time << '\n';
}
