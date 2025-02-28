#include <iostream>
using namespace std;

// Define a function called common_letters here.

// Do not change anything below.
int main() {
    cout << common_letters("apple", "leaves") << "\n";
    cout << common_letters("chocolate", "catching") << "\n";
    cout << common_letters("chocolate", "chocolate") << "\n";
    cout << common_letters("chocolate", "banana") << "\n";
    cout << common_letters("chocolate", "drums") << "\n";
    cout << common_letters("tree", "e") << "\n";
    cout << common_letters("", "x") << "\n";
    cout << common_letters("oooooooooo", "ooo") << "\n";
    cout << common_letters("shshshshshshshsh", "shake") << "\n";
    cout << common_letters("pneumonoultramicroscopicsilicovolcanoconiosis",
                           "methylenedioxymethamphetamine")
         << "\n";
}
