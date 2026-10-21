// @check-accepted: *
#include <iostream>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

int main() {

    string sor;
    getline(cin, sor);

    stringstream ss(sor); // Automatikusan daraboljuk a szöveget
    // szóközök (vagy a getline segítségével más karakterek, pl. vessző) mentén.
    stack<int> st;

    string token;
    while (ss >> token) { // kiveszi a stringstreamből az első elemet

        // Operátor?
        if (token == "+" || token == "-" || token == "*" || token == "/") {

            int b = st.top();
            st.pop();

            int a = st.top();
            st.pop();

            if (token == "+") {
                st.push(a + b);
            } else if (token == "-") {
                st.push(a - b);
            } else if (token == "*") {
                st.push(a * b);
            } else {
                st.push(a / b);
            }
        } else {
            // Szám
            st.push(stoi(token));
        }
    }
    cout << st.top() << endl;
    return 0;
}
