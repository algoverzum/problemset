#define CMS
#include "testlib.h"

#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int solPilots = ans.readInt();
    int userPilots = ouf.readInt();

    if (solPilots != userPilots)
        quit(_wa, "wrong");
    else if (solPilots == 0) {
        quit(_ok, "ok");
    } else {
        int K = inf.readInt();
        int N = inf.readInt();
        vector<pair<int, int>> pilots;
        for (int i = 0; i < N; i++) {
            int s = inf.readInt();
            int e = inf.readInt();
            pilots.emplace_back(s, e);
        }
        vector<int> userSol;
        for (int i = 0; i < userPilots; i++) {
            if (ouf.seekEof())
                quitp(0.5, "partial");
            int p = ouf.readInt();
            p--;
            if ((p < 0) || (p >= N))
                quitp(0.5, "partial");
            userSol.push_back(p);
        }
        if (pilots[userSol[0]].first != 0)
            quitp(0.5, "partial");
        if (pilots[userSol[userPilots - 1]].second != K)
            quitp(0.5, "partial");
        for (int i = 0; i < userPilots - 1; i++) {
            if (pilots[userSol[i]].second < pilots[userSol[i + 1]].first)
                quitp(0.5, "partial");
            if (pilots[userSol[i]].first > pilots[userSol[i + 1]].second)
                quitp(0.5, "partial");
        }
        quit(_ok, "ok");
    }
}
