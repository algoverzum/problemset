## Coins
In a special country, there are two types of coins in circulation. One coin has a value of 2 petaks, and the other has a value of $K$ petaks, where $K \ne 2$.

The question is whether it is possible to pay exactly $N$ petaks using these coins. In other words, determine whether there exist non-negative integers $x$ and $y$ such that $2\cdot x+K\cdot y=n$ holds.

### Input
The first line of the input contains a single integer $N$, the amount to be paid.

The second line of the input contains a single integer $K$, the value of the other coin.

### Output
Print `YES` if the amount of $N$ petaks can be paid exactly using the given coins. Otherwise, print `NO`.

### Constraints
* $1 \le N, K \le 10^{18}$
* $K \not= 2$

### Example 1 input
    5
    3

### Example 1 output
    YES

### Explanation of Example 1
You can use one coin of value 2 and one coin of value $K = 3$.

### Example 2 input
    6
    1

### Example 2 output
    YES

### Explanation of Example 2
You can use three coins of value 2.
Alternatively, you can use six coins of value $K = 1$.

### Example 3 input
    7
    4

### Example 3 output
    NO


### Example 4 input
    5
    7

### Example 4 output
    NO

