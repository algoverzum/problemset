## Cities
You need to catalog a distant star system. To do this, you have a list where each line contains the name of a planet, followed by the cities located on it. Additionally, you have another list containing city names, and your task is to determine which planet each city belongs to.

### Input
The first line of the input contains an integer: $N$ the number of planets.
The next $N$ lines each contain the name of a planet, followed by the cities located on it, separated by spaces.
The $N+2$-th line contains an integer: $M$ the number of queried cities.
Each of the next $M$ lines contains a single city name. Each city is guaranteed to be present on one of the planets.
Planet and city names consist only of lowercase English letters and are at most 10 characters long.
A planet can have at most 1000 cities.

### Output
Print $M$ planet names, each on a separate line. These are the planets where the queried cities are located.

### Constraints
* $1 \le N,M \le 1000$

### Example input
    4
    mandalore sundari ronion
    naboo theed keren vis
    alderaan aldera juranno
    kamino tipoca
    3
    tipoca
    theed
    aldera

### Example output
    kamino
    naboo
    alderaan

### Explanation of the example
tipoca is on kamino.
theed is on naboo.
aldera is on alderaan.
