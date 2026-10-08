// @check-accepted: *
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        pq.push(x);
    }

    long long osszeg = 0;

    while (pq.size() > 1) {
        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();

        int c = a + b;
        osszeg += c;

        pq.push(c);
    }

    cout << osszeg << "\n";

    return 0;
}