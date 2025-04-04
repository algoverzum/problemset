#define CMS
#include "testlib.h"
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);

    int N = inf.readInt(); // állomások száma
    int H = inf.readInt(); // hatósugár
    inf.readEoln();
    vector<int> stations(N);
    for (int i = 0; i < N; ++i) {
        stations[i] = inf.readInt();
    }

    // Hivatalos megoldásból csak az első sor kell
    int opt_K = ans.readInt();
    // ans.readEoln();
    // vector<int> opt_pos(opt_K);
    // for (int i = 0; i < opt_K; ++i) {
    //   opt_pos[i] = ans.readInt(1, N);
    // }

    // Versenyző megoldása
    int user_K = ouf.readInt();
    ouf.readEoln();
    vector<int> user_pos(user_K);
    for (int i = 0; i < user_K; ++i) {
        user_pos[i] = ouf.readInt(1, N);
    }

    // 1. Ellenőrizzük, hogy minden generátor érvényes pozíción van
    set<int> station_set(stations.begin(), stations.end());
    for (int p : user_pos) {
        if (!station_set.count(stations[p - 1])) {
            quitf(_wa, "A generátor (%d) nem érvényes állomáshelyen van.", p);
        }
    }

    // 2. Ellenőrizzük, hogy minden állomás le van fedve
    sort(user_pos.begin(), user_pos.end());

    int g = 0;
    for (int i = 0; i < N; ++i) {
        int pos = stations[i];

        // Haladjunk, amíg g generátor túl van a pozíción
        while (g < user_K && abs(stations[user_pos[g] - 1] - pos) <= H) {
            g++;
        }
    }
    if (g < user_K) {
        quitf(_wa, "Az állomás (%d) nincs lefedve.", g);
    }

    // 3. Optimalitás
    if (user_K > opt_K) {
        quitf(_wa,
              "Nem optimális megoldás: %d generátor, de a legjobb %d "
              "generátorral megoldható.",
              user_K, opt_K);
    }
    if (user_K < opt_K) {
        quitf(_wa, "Túl szép, hogy igaz legyen.");
    }

    quitf(_ok, "Helyes megoldás, %d generátorral.", user_K);
}
