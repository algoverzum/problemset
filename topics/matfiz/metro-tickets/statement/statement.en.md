## Tom and the Metro Tickets – Sum of Coin Pairs

Tom is visiting Jenny and decided to take the subway.  
The ticket can only be purchased at a machine that accepts **exactly two coins** whose sum does not exceed $k$.

Tom has coins in both of his pockets.  
His left pocket contains $n$ coins: their values are $b_1, b_2, \dots, b_n$.  
His right pocket contains $m$ coins: their values are $c_1, c_2, \dots, c_m$.

He wants to choose exactly **one** coin from his left pocket and **one** coin from his right pocket.  
Help Tom determine how many ways he can choose the indices $f$ and $s$ such that:

\[
b_f + c_s \le k
\]

### Input
The first line: an integer $t$ &ndash; the number of test cases.

The first line of each test case contains three integers: $n$, $m$, and $k$ &ndash; the number of coins in the left pocket, the number of coins in the right pocket, and the maximum sum of the two coins needed to pay for the ticket at the machine.

The second line of each test case contains $n$ integers, where $b_1, \dots, b_n$ are the denominations of the coins in the left pocket.

The third line of each test case contains $m$ integers: the coins in the right pocket, $c_1, \dots, c_m$.

### Output
For each test case, print a single line:  
the **number of valid index pairs** for the two chosen coins where the condition is met:
\[b[i] + c[j] \le k \].

That is, print how many ways Tom can select two coins, taking one from each pocket, such that their sum does not exceed $k$.


### Constraints
- $1 \le t \le 100$
- $1 \le n, m \le 100$
- $1 \le k \le 2000$
- $1 \le b_i \le 1000$
- $1 \le c_i \le 1000$

### Sample Input
    4
    4 4 8
    1 5 10 14
    2 1 8 1
    2 3 4
    4 8
    1 2 3
    4 2 7
    1 1 1 1
    2 7
    3 4 2000
    1 1 1
    1 1 1 1

### Sample Output
    6
    0
    4
    12


### Explanation of the Sample

Note that the pairs represent the **indices** of the coins in the array, not their denominations!

#### Test Case 1
In the first test case, Tom can choose the following coin pairs: $[1,1], [1,2], [1,4], [2,1], [2,2], [2,4]$, making a total of **6**.

#### Test Case 2
There is no pair where $b[i] + c[j] \le 4$ → **0**.

#### Test Case 3
Valid pairs are: $[1,1], [2,1], [3,1], [4,1]$ → **4**.

#### Test Case 4
Every left-side coin can be combined with all 4 right-side coins → 3×4 = **12**.
