## Three Digit Before
On our planet, we play Bingo with the presenter drawing lots for you until zero comes out. Then the game ends, and the winner is the one with the most numbers on their ticket. Your ticket contains all three-digit numbers. Can you tell me how many of your numbers were drawn?


### Input
The first line of the input contains $N$ - the 
The input contains integers, one number per line. The number in the $i$th row is the $i$th drawn number. The last line is guaranteed to be a zero.

### Output
You have to write a single number, the number of three-digit numbers.

### Constraints
* in the $i$th line you can found the number $S_i$, such that $0 \le S_i \le 1\,000,\000$. If $i!=j$ then $S_i!=S_j$.
* the number of non-empty lines is $N$, where $1 \le N \le 1000$.

### Example input
    5
    123
    12345
    12
    555
    678
    2
    0

### Example output
    3

### Explanation of the example
    There were 3 three-digit numbers before the zero: 123, 555, 678.
