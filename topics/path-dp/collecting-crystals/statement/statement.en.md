## Collecting Crystals
Each field on the grid map of an uncharted planet surface, consisting of $N$ rows and $M$ columns, contains either a dangerous trap or valuable energy crystals. A Starfleet officer's task is to move through the grid, starting from the top left corner and reaching the bottom right corner, while collecting as many crystals as possible. The rules of the mission are as follows:

- Do not enter the trap field, as it endangers the officer's life.

- The officer can only move to the right or downwards in each step.

- The officer collects all energy crystals from any fields he steps on.

Mission Goal: Create a program that calculates the maximum number of energy crystals that a Starfleet officer can collect, and gives the optimal path that will result in the most crystals.
If traps prevent him from reaching the bottom right corner, $-1$ should be printed. If multiple paths are possible, any one can be entered.

### Input
The first line of the input contains two space-separated integers, $N$ and $M$, the number of rows and columns of the surface grid map.

An additional $N$ lines follow, each containing $M$ integers, the number of energy crystals in the cells of the map, or $-1$ if there is a trap. The $i$-th row is the $j$-th number $A_{i,j}$.

### Output
In the first line of the output, you must enter a single number, the maximum number of energy crystals you can obtain. If you cannot get to the bottom right corner, write $-1$.

If you can get to the bottom right corner, then in the second line of the output, enter the way to get there. Specify the path with a string of $N+M-2$ characters, where the $i$-th character should be $R$ if you move to the right in the $i$-th step. And if we move down, the character is $D$. 

### Constraints
* $1 \le N, M \le 1000$
* $-1 \le A_{i,j} \le 10000$ for each $i,j$
* $A_{1,1} \not= -1$
* $A_{N,M} \not= -1$

### Example 1 input
    5 6
    1 2 3 4 0 1
    2 -1 2 1 -1 3
    -1 0 6 0 0 0
    4 1 0 -1 1 -1
    0 0 1 2 0 0

### Example 1 Output
    17
    RRDDDDRRR

### Explanation of example 1
It is easy to check that this is the best of the 4 possible routes. 

### Example 2 input
    3 3
    1 2 -1
    2 -1 2
    -1 0 6

### Example 2 Output
    -1

### Explanation of example 2
You cannot get from the top left field to the bottom right field.
