// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> titles;
    vector<int> years;

    for (int i = 0; i < N; i++) {
        string title;
        int year;
        cin >> title >> year;
        titles.push_back(title);
        years.push_back(year);
    }

    // Indexek vektorának létrehozása és rendezése
    vector<int> indices(N);
    for (int i = 0; i < N; i++) {
        indices[i] = i;
    }

    sort(indices.begin(), indices.end(), [&](int i, int j) {
        if (years[i] == years[j]) {
            return titles[i] < titles[j];
        }
        return years[i] < years[j];
    });

    // Kiírás a rendezett sorrendben
    for (int idx : indices) {
        cout << titles[idx] << " " << years[idx] << endl;
    }

    return 0;
}
