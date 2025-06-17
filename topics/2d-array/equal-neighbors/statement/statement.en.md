## Equal Neighbors
Your space crew has landed on a mysterious planet. In one of the caves, you find a grid full of strange signal readings left behind by aliens. The signals are written in a table, where each cell has a number.

Sometimes, two neighboring cells (next to each other up, down, left, or right) have exactly the same signal. These are called echo signals.

Your job is to count how many cells have at least one neighbor with the same number.

### Input
The first line of the input contains two integers: the number of rows $N$ and the number of columns $M$.
The next $N$ rows each contain $M$ integers: $S_{i,j}$, the signal value in the $(i,j)$-th cell.

### Output
Print one number: how many cells have at least one neighbor with the same value.

### Constraints
* $1 \le N, M \le 100$
* $1 \le S_{i,j} \le 1000$

### Example input
    4 3
    2 1 5
    5 3 5
    2 2 2
    9 6 7

### Example output
    5

### Explanation of the example

Cells with at least one matching neighbor:

* (1,3) and (2,3): neighboring cells containing 5.

* (3,1), (3,2), (3,3): all are 2 and next to each other.
