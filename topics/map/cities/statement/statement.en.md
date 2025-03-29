## Cities
You need to catalog a distant star system. To do this, you have a list where each line contains the name of a planet, followed by the cities located on it. Additionally, you have another list containing city names, and your task is to determine which planet each city belongs to.

### Input
The first line of the input contains an integer: $N$ the number of planets.<br>
The next $N$ blocks each consist of two lines:<br>
* The first line contains the name of a planet and an integer indicating the number of cities on that planet.<br>
* The second line lists the names of the cities on that planet, separated by spaces.

The next ($2N+1$-th) line contains an integer: $M$ the number of queries.<br>
Each of the next $M$ lines contains a single city name. Each city is guaranteed to be present on one of the planets.
Planet and city names consist only of lowercase English letters and are at most 10 characters long.
A planet can have at most 1000 cities.

### Output
Print $M$ planet names, each in a separate line. These are the planets where the queried cities are located.

### Constraints
* $1 \le N,M \le 1000$

### Example input
    4
    mandalore 2
    sundari ronion
    naboo 3
    theed keren vis
    alderaan 2
    aldera juranno
    kamino 1
    tipoca
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
