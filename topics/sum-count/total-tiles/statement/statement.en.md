## Total Tiles
Our king, Baltasar has a castle with $N$ rooms. Every room has a square shape, and the side length of each room is an integer number. Baltasar wants to put new floor tiles to every room. The new tiles have a square shape with side length 1. How many new tiles will he need in total?

### Input
The first line of the input contains $N$ - the number of rooms. Each of the following $N$ lines contains a single number $S_i$ - the side length of a room ($i =1, 2, \ldots, N$).  

### Output
Print a single number, the total number of floor tiles Baltasar has to buy.

### Constraints
* $1 \le N \le 100$
* $1 \le S_i \le 100$

### Example input
    4
    3
    4
    1
    4

### Example output
    42

### Explanation of the example
There are 4 rooms with sizes 3, 4, 1, 4, and for covering their floors Baltasar needs $3 \cdot 3 = 9, 1 \cdot 1 = 1, 4 \cdot 4 = 16, 4 \cdot 4 = 16$ tiles respectively, in total 42.   
