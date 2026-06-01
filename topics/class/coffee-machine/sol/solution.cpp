// @check-accepted: *
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

    CoffeeMachine(string cur_brand) {
        brand = cur_brand;
        is_on = false;
        water_ml = 0;
        coffee_g = 0;
    }

    void set_electricity(bool state) { is_on = state; }

    void add_water(int amount) { water_ml += amount; }

    void add_coffee(int amount) { coffee_g += amount; }

    bool brew_coffee() {
        if (is_on && water_ml >= 50 && coffee_g >= 15) {
            water_ml -= 50;
            coffee_g -= 15;
            return true;
        }
        return false;
    }

    string get_status() {
        return brand + " " + (is_on ? "ON" : "OFF") + " " +
               to_string(water_ml) + "ml " + to_string(coffee_g) + "g";
    }
};

// Do not change anything below.
int main() {
    string name;
    cin >> name;

    CoffeeMachine CM(name);

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
            CM.add_water(water);
        } else if (cur == 4) {
            int coffee;
            cin >> coffee;
            CM.add_coffee(coffee);
        } else if (cur == 5) {
            CM.brew_coffee();
        } else if (cur == 6) {
            cout << CM.get_status() << '\n';
        }
        cin >> cur;
    }
    return 0;
}
