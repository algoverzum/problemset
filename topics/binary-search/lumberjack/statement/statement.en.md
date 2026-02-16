## Lumberjack
A forestry company needs to collect at least $M$ meters of wood from a row of trees with given heights. They use a cutting machine where a cutting height $H$ can be set: the machine cuts off every part of a tree that is above height $H$, while trees not taller than $H$ remain unchanged. The collected pieces form the total amount of harvested wood.

The goal is to determine the maximum integer value of $H$ such that the total length of the cut wood is at least $M$ meters.

### Input
The first line contains: $N$ (number of trees) and $M$ (required wood length).  
The second line contains $N$ positive integers $A_1, A_2, \ldots, A_N$ — the heights of the trees.

### Output
The maximum integer cutting height $H$ such that the total length of the cut wood is at least $M$ meters.

### Constraints
* $1 \le N \le 10^5$
* $1 \le M \le 2\cdot 10^{9}$
* $1 \le A_i \le 10^9$ for all $i = 1, 2, \ldots, N$
* $A_1 + A_2 + \ldots + A_n \ge M$

### Example Input 1
    4 7
    15 10 5 12

### Example Output 1
    10

### Explanation of Example 1
For example, if the trees have heights 15, 10, 5, and 12 meters and the cutting height is set to 10 meters, then the remaining tree heights will be 10, 10, 5, and 10 meters. The machine cuts 5 meters from the first tree and 2 meters from the fourth tree (a total of 7 meters).

### Example Input 2
    5 20
    14 52 50 36 56

### Example Output 2
    46
