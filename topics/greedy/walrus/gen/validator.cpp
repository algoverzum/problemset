#include "testlib.h"

#include <iostream>
#include <utility>
#include <vector>
#include <cmath>

using namespace std;
const int NMAX=3e5,TMAX=1e4,VMAX=1e9;

int main(int argc, char* argv[])
{
    freopen(argv[1], "r", stdin);
    registerValidation(argc,argv);
    int t=inf.readInt(1,TMAX,"t"),s=0;
    inf.readEoln();
    for(int tid=1;tid<=t;tid++){
        setTestCase(tid);
        int n=inf.readInt(1,NMAX,"n");
        s+=n;
        ensuref(s<=NMAX,"sum of n exceeds %d",NMAX);
        inf.readEoln();
        string s=inf.readToken();
        ensuref(s.size()==n,"string length does not correspond to n");
        bool sleeping=0;
        for(auto it : s){
            ensuref(it=='.' || it=='-',"Invalid character %c detected",it);
            if(it=='.') sleeping=1;
        }
        ensuref(sleeping,"No walruses are sleeping");
        inf.readEoln();
    }
    inf.readEof();
    return 0;
}
