// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> egyesek = {"",   "egy", "ketto", "harom", "negy",
                              "ot", "hat", "het",   "nyolc", "kilenc"};
    vector<string> tizesek = {"",         "tizen",    "huszon", "harminc",
                              "negyven",  "otven",    "hatvan", "hetven",
                              "nyolcvan", "kilencven"};
    if (n == 10)
        cout << "tiz";
    else if (n == 20)
        cout << "husz";
    else
        cout << tizesek[n / 10] << egyesek[n % 10];
    cout << "\n";
    return 0;
}
