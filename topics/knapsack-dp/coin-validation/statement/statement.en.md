## Coin Validation
On the planet Zorblax, the government has introduced a new coin system. This consists of $N$ different coin types, which will be produced in large quantities. Your task is to validate this system by determining whether some amounts can be paid using the available coins (using any number of each type).

### Input
The first line of the input contains $N$ and $Q$ — the number of different coin types and the number of amunts to check.  
The second line contains $N$ integers, representing the values of the coin types ($C_i$).  
The next $Q$ lines each contain a single integer $X_j$, representing the amounts to check.

### Output
For each query, print `YES` if the amount $X_i$ can be paid using the available coins, otherwise print `NO`.

### Constraints
* $1 \le N \le 100$
* $1 \le Q \le 100\,000$
* $1 \le C_i \le 100\,000$ for all $i=1 \dots N$
* $1 \le X_j \le 100\,000$ for all $j=1 \dots Q$

### Example input
    2 4
    2 4
    6
    7
    8
    10

### Example output
    YES
    NO
    YES
    YES

### Explanation of the example
The available coin types are 2, and 4.  
- For $X = 6$, it can be paid as $2 + 4$.  
- For $X = 7$, it cannot be paid using any combination of the coins.  
- For $X = 8$, it can be paid as $4 + 4$.  
- For $X = 10$, it can be paid as $2 + 4 + 4$.
