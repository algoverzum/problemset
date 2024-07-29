#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if(n<10)
    {
        cout<<0<<"\n";
    }
    else
    {

        cout << (n/10)%10 << "\n";
    }

    return 0;
}
