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
    // Initializes this CoffeeMachine with brand.
    // Sets is_on to False, water_ml to 0, and coffee_g to 0.
    CoffeeMachine(string brand) {
        // Write your code here
    }

    // Changes the power status (is_on) of self to state.
    void set_electricity(bool state) {
        // Write your code here
    }

    // Adds the given amount to the machine's water level (water_ml).
    void add_water(int amount) {
        // Write your code here
    }

    // Adds the given amount to the machine's coffee level (coffee_g).
    void add_coffee(int amount) {
        // Write your code here
    }

    // Checks if the machine is on (is_on is true),
    // has at least 50 ml water, and at least 15 g coffee.
    // If all conditions are met, deducts 50 from water and 15 from coffee,
    // then returns true. Otherwise, returns false.
    bool brew_coffee() {
        // Write your code here
    }

    // Returns a formatted string with the machine's brand,
    // power status (ON/OFF), current water in ml, and coffee level in g.
    // Example: "ABC ON 100ml 5g" if the brand is ABC, the machine is turned
    // on, contains 100 ml of water, and 5 g of coffee Write your code here
    string get_status() {
        // Write your code here
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
