## Scale A Matrix
The Jedi Archives store battle strategy matrices to help the Republic plan its defenses. Each matrix consists of $N$ rows and $M$ columns, representing tactical values.

Your mission is to enhance a given matrix by multiplying each value with a Force amplification factor $C$.

### Input
The first line contains two integers, $N$ (number of rows) and $M$ (number of columns).
The next $N$ lines contain $M$ integers each, representing the matrix values.
The final line contains an integer $C$, the Force amplification factor.

### Output
Print the transformed matrix, where each element is multiplied by $C$.

### Constraints
* $1 \le N, M \le 10$
* $-100 \le C \le 100$
* the values of the matrix are between $-100$ and $100$ as well.

### Example input
    3 4
    11 12 13 14
    21 22 23 24
    31 32 33 34
    2

### Example output
    22 24 26 28
    42 44 46 48
    62 64 66 68
