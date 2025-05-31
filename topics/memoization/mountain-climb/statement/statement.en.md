## Mountain Climb
Explorers try to map a mountain on the planet. The different areas of the mountain are represented by a square grid, where the values in each box represent the height of the area. The two sides of the square grid have the same length. The researchers start from one area on the edge of the mountain and move in one step to an adjacent (non-diagonal) area exactly one higher. The explorers continue upwards in this way until they reach a point from which they can go no higher, where they end their expedition. Create a program that gives the longest distance that the explorers can travel to the end of their expedition.

### Input
The first line of the input contains a single integer, the length of the side of the square containing the mountain: $N$.
The next $N$ row contains $N$ integers, the height of each mountain area: $ A_{1,1}, A_{2,1}, \ldots, A_{N,1}, A_{1,2}, \dots, A_{N,N}$ 

### Output
In the first line of the output, print a single integer, the length of the longest expedition.
In the second line of the output, print two integers, the starting point of the longest expedition.

### Constraints
* $1 \le N \le 30$
* $1 \le A_{i,j} \le 30$

### Example input
    6
    1 2 2 2 2 2
    4 3 4 2 2 1
    1 1 5 6 1 8
    1 1 1 9 6 7
    1 3 4 4 5 1
    1 2 1 1 1 1

### Example output
    5
    1 1

### Explanation of the example
Starting from the top left corner, the longest path is to field (3,4).
