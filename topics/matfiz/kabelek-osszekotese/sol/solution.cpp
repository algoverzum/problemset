// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;

    priority_queue<int, vector<int>,
                   greater<int>> pq; // min-heap

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        pq.push(x);
    }

    int koltseg = 0;

    while (pq.size() > 1) {

        int a = pq.top();
        pq.pop();

        int b = pq.top();
        pq.pop();

        int uj = a + b;

        koltseg += uj;

        pq.push(uj);
    }

    cout << koltseg << endl;

    return 0;
}