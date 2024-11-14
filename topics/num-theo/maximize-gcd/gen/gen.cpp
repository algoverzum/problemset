#include "testlib.h"
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cassert>

using namespace std;

int main(int argc, char* argv[])
{
    registerGen(argc, argv, 1);
   
    int t = atoi(argv[1]);
    int nmax = atoi(argv[2]);
    
    cout << t << endl;
    
    while (t) {
        int a = rnd.next(1, nmax);
        int b = rnd.next(1, nmax);
        int k = rnd.next(1, nmax);
        cout << a << " " << b << " " << k << endl;
        t--;
    }
    
    return 0;
        
}
