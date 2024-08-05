// @check-accepted: *
#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    if (a % 2 == 1)
    {
        cout << 1 << endl;
    }
    else
    {
        if (b % 2 == 1)
        {
            cout << 1 << endl;
        }
        else
        {
            cout << -1 << endl;
        }
    }
}
