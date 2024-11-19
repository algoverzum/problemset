/**
 *    author:  BERNARD B.01
 **/
#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    const int subtask_no = atoi(argv[1]);
    const int tt = atoi(argv[2]);
    const int MAXN = atoi(argv[3]);
    const int SUMN = atoi(argv[4]);
    const int MAXM = atoi(argv[5]);
    println(tt);
    vector<int> ns = rnd.partition(tt, SUMN, 1);
    vector<int> ms = rnd.partition(tt, MAXM, 1);
    for (int qq = 0; qq < tt; qq++) {
        println("");
        int n = (MAXN == 1 ? 1 : ns[qq]), m = ms[qq];
        println(n, m);
        for (int i = 0; i < n; i++) {
            string s(m, '0');
            for (int j = 0; j < m; j++) {
                s[j] += rnd.next(0, 1);
            }
            println(s);
        }
    }
    return 0;
}
