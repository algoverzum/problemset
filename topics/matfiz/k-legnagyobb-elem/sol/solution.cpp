// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {

    int n, k;
    cin >> n >> k;

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if ((int)pq.size() < k) {
            pq.push(x);
        } else if (x > pq.top()) {
            pq.pop();
            pq.push(x);
        }
    }

    vector<int> eredmeny;
    while (!pq.empty()) {
        eredmeny.push_back(pq.top());
        pq.pop();
    }
    for (int i = (int)eredmeny.size() - 1; i >= 0; i--) {
        cout << eredmeny[i];
        if (i > 0) {
            cout << " ";
        }
    }
    cout << endl;
    return 0;
}
