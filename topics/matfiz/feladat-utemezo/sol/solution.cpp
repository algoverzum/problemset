// @check-accepted: *
#include <iostream>
#include <queue>

using namespace std;

struct Feladat {
    char nev;
    int prioritas;
    int sorszam; // beolvasási sorrend
};

// Max-heap: a nagyobb prioritás kerüljön előre
struct Compare {
    bool operator()(const Feladat &a, const Feladat &b) const {
        if (a.prioritas != b.prioritas)
            return a.prioritas < b.prioritas; // nagyobb prioritás előre
        return a.sorszam > b.sorszam;
    }
};

int main() {
    priority_queue<Feladat, vector<Feladat>, Compare> pq;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        Feladat f;
        cin >> f.nev >> f.prioritas;
        f.sorszam = i;
        pq.push(f);
    }
    while (!pq.empty()) {
        cout << pq.top().nev << "\n";
        pq.pop();
    }
}