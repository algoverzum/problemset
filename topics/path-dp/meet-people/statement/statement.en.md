## Meet People
In a far away galaxy Spock is navigating in a sector of space, represented by a grid of star systems. Each square of this grid corresponds to a star system, and each system has a varying number of crew members from the USS Enterprise, or perhaps other starships, stationed there.

Spock's mission is to travel from the left edge of the grid (starting from any  star system) and reach the right edge of the sector (any star system). At each step, Spock has several options:

* Move Right: Spock can move straight ahead to the next system in the same row.
* Move Up to the Right: Spock can move diagonally upward-right to a system one row higher and one column to the right.
* Move Down to the Right: Spock can move diagonally downward-right to a system one row lower and one column to the right.

Spock must carefully plan his course through the sector. The **goal** is to maximize the number of crew members he meets along the way as he travels from left to right. He cannot leave the grid, and each system he visits he meets all crew members there.

### Input
In the input, the first line contains two integers, the number of rows and columns: $N$, $M$.
The subsequent $N$ row has $M$ integers, the number of people in the $i$-th row and $j$-th column is $P_{i,j}$.

### Output
In the first line of the output, you need to print an integer: how many crew members we Spock meet.
In the second line of the output you have to print an integer: from which line we have to start for this. If there are multiple solutions print the smallest index. (The indexing starts from 1.)

### Constraints
* $1 \le N,M \le 100$
* $0 \le P_{i,j} \le 1000$

### Example input
    4 4
    6 1 7 1
    1 6 1 7
    2 2 2 2
    9 1 1 9

### Example output
    26
    1

### Explanation of the example
We visit the following spaces ($6+6+7+7=26$):

<b>6</b> 1 <b>7</b> 1

1 <b>6</b> 1 <b>7</b>

2 2 2 2

9 1 1 9
