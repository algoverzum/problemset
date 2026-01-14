## Solar System
The people of our planet wonder how many celestial bodies there are in our solar system. To do this, we've collected how many moons each planet in the solar system has. Create a program that can determine how many celestial bodies there are in the solar system from a list of the number of moons of the planets. (For the purposes of this exercise, we will count only moons, planets and stars as celestial bodies and assume that there is only one star in the middle of the solar system.)

### Input
The first line of the input contains single integer, the number of planets $N$
The next $N$ lines contain a single integer each, the number of moons of the $N$th planet: $A_1, A_2, \dots, A_N$ 

### Output
Print a single number, the number of celestial bodies in the solar system.

### Constraints
* $1 \le N \le 100$
* $0 \le A_i \le 1000$

### Example input
    8
    0 0 1 2 9 14 3 14

### Example output
    52

### Explanation of the example
The total number of moons is 43 and if we add 8 planets and one star, we get 52 celestial bodies.
