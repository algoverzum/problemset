#include <iostream>
#include <string>
using namespace std;

class CoffeeMachine {
  private:
    bool is_on;
    int water_ml;
    int coffee_g;

  public:
    string brand;

    CoffeeMachine(string brand) {
        // Write your code here
    }

    void set_electricity(bool state) {
        // Write your code here
    }

    void set_water(int amount) {
        // Write your code here
    }

    void set_coffee(int amount) {
        // Write your code here
    }

    bool brew_coffee() {
        // Write your code here
    }

    string get_status() {
        // Write your code here
    }
};

// Do not change anything below.
int main() {
    string name;
    cin >> name;

    CoffeeMachine CM(name);

    bool ok = true;

    try {
        int cur;
        cin >> cur;

        while (cur != 0) {
            if (cur == 2) {
                int on;
                cin >> on;

                if (on == 1)
                    CM.set_electricity(true);
                else
                    CM.set_electricity(false);
            } else if (cur == 3) {
                int water;
                cin >> water;
                CM.set_water(water);
            } else if (cur == 4) {
                int coffee;
                cin >> coffee;
                CM.set_coffee(coffee);
            } else if (cur == 5) {
                CM.brew_coffee();
            } else if (cur == 6) {
                cout << CM.get_status() << endl;
            }

            cin >> cur;
        }
    } catch (...) {
        ok = false;
    }

    if (ok)
        cout << "OK\n";
    else
        cout << "HIBA\n";

    return 0;
}
