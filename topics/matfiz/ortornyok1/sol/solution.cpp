#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int N, M;

const int MAX = 21;
bool tiltott[MAX][MAX];

vector<int> aktualis;
vector<vector<int>> megoldasok;

/*
    Eldönti, hogy az idx torony
    hozzáadható-e a jelenlegi őrbeosztáshoz.
*/
bool lehet(int idx) {
    for (int i = 0; i < aktualis.size(); i++) {
        if (tiltott[idx][aktualis[i]]) {
            return false;
        }
    }

    return true;
}

/*
    Backtracking
*/
void backtrack(int idx) {
    if (idx > N) {
        megoldasok.push_back(aktualis);
        return;
    }

    // 1. ág: bevesszük
    if (lehet(idx)) {
        aktualis.push_back(idx);
        backtrack(idx + 1);
        aktualis.pop_back();
    }

    // 2. ág: nem vesszük be
    backtrack(idx + 1);
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;

        tiltott[a][b] = true;
        tiltott[b][a] = true;
    }

    backtrack(1);

    // lexikografikus rendezés
    sort(megoldasok.begin(), megoldasok.end());

    cout << megoldasok.size() << "\n";

    for (int i = 0; i < megoldasok.size(); i++) {
        for (int j = 0; j < megoldasok[i].size(); j++) {
            if (j > 0) {
                cout << " ";
            }

            cout << megoldasok[i][j];
        }

        cout << "\n";
    }

    return 0;
}