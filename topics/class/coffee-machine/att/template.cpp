#include <iostream>
#include <string>
using namespace std;

class CoffeeMachine {
  private:
    string brand;
    bool is_on;
    int water_ml;
    int coffee_g;

  public:
    CoffeeMachine(string brand) {
        // Initializes self with brand.
        // Sets is_on to False, water_ml to 0, and coffee_g to 0.
        // Write your code here
    }

    void set_electricity(bool state) {
        // state is a boolean (True/False).
        // Changes the power status (is_on) of self to state.
        // Write your code here
    }

    void add_water(int amount) {
        // Adds the given amount to the machine's water level (water_ml).
        // Write your code here
    }

    void add_coffee(int amount) {
        // Adds the given amount to the machine's coffee level (coffee_g).
        // Write your code here
    }

    bool brew_coffee() {
        // Checks if the machine is on (is_on is True),
        // has at least 50 ml water, and at least 15 g coffee.
        // If all conditions are met, deducts 50 from water and 15 from coffee,
        // then returns True. Otherwise, returns False.
        // Write your code here
    }

    string get_status() {
        // Returns a formatted string with the machine's brand,
        // power status (ON/OFF), current water in ml, and coffee level in g.
        // Example: "ABC ON 100ml 5g" if the brand is ABC, the machine is turned
        // on, contains 100 ml of water, and 5 g of coffee Write your code here
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
            cout << CM.get_status() << endl;
        }

        cin >> cur;
    }
    return 0;
}
