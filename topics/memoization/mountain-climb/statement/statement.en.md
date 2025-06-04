## Mountain Climb
Imagine you're an explorer on a planet with mountains that look like they were artificially constructed from giant cubes! The terrain is mapped as a square grid. Each cell in this grid contains a number representing the height of the stack of cubes at that location.

Your mission is to find the longest possible climbing path by adhering to the following rules:

* Starting Point: Your climb must begin at an area (a cell) located on the edge of the grid. This means it must be in the first row, last row, first column, or last column.
* Movement: In each step, you can move from your current area to an adjacent one (up, down, left, or right). (Diagonal moves are not allowed).
* Ascending Rule: You can only move to an adjacent area if its height is exactly one unit greater than the height of your current area (e.g., from a stack of $H$ cubes to an adjacent stack of $H+1$ cubes).
* Path End: You must continue this upward climb as long as possible. The expedition for a particular path ends when you reach an area from which no further moves can be made according to the Ascending Rule.

Goal: Write a program that determines the maximum number of steps an explorer can take in a single expedition. Remember, the path must start on the border and follow all the rules above. If no such valid path can be started, the longest distance is 0 steps.

### Input
The first line of the input contains a single integer $N$: the size of the square grid.  
The next $N$ lines each contain $N$ integers — the elevation values of the cells. The elevation of the $i$th row and $j$th column is $A_{i,j}$.

### Output
The output should consist of two lines:

* The first line contains a single integer: the length of the longest possible path.
* The second line contains two integers: the starting point of the longest expedition (row and column).

If there are multiple starting cells, then any of them can be chosen.

### Constraints
* $1 \le N \le 500$
* $1 \le A_{i,j} \le 10^6$ for each $1 \le i,j \le N$

### Example input
    6
    5 1 6 1 5 4
    4 2 5 2 3 5
    3 3 4 9 4 5
    2 4 3 4 4 6
    1 5 4 5 5 4
    2 3 5 9 6 5

### Example output
    5
    1 2

### Explanation of the example
Starting from first row's second and fouth cell is possible to get a path $1\to 2\to 3\to 4\to 5\to 6$.
