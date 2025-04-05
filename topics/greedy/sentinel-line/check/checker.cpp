#define CMS
#include "testlib.h"
#include <algorithm>
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

    // Ellenőrizzük, hogy minden állomás le van fedve
    sort(user_pos.begin(), user_pos.end());

    int g = 0;
    int i = 0;
    while (i < N && g < user_K) {
        int pos = stations[i];
        if (g < user_K && abs(stations[user_pos[g] - 1] - pos) <= H) {
            i++;
        } else {
            g++;
        }
    }
    if (i < N) {
        quitf(_wa, "Az állomás (%d) nincs lefedve.", i + 1);
    }

    // Optimalitás
    if (user_K > opt_K) {
        quitf(_wa,
              "Nem optimális megoldás: %d generátor, de a legjobb %d "
              "generátorral megoldható.",
              user_K, opt_K);
    }
    if (user_K < opt_K) {
        quitf(_wa, "Túl szép, hogy igaz legyen OR Official solution broken.");
    }

    quitf(_ok, "Helyes megoldás");
}
