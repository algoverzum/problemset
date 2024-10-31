## Bets
On the planet Appaloosa, you bet on horse races on $N$ days. At the end of each day, you record how much money you have. To make your bets better next time, you calculate how much your money has changed on consecutive days, and then calculate how much your consecutive money changes have changed.

### Input
The falling line of the input is an integer: $N$  
Then the next line contains $N$ of numbers $A_1, A_2, __ldots, A_{N}$.

### Output
You have to print two lines, both with the numbers separated by spaces
In the first line, the difference between your money on consecutive days
In the second line, the difference between the consecutive differences

### Limits
* $1 \le N \le 100$
* $1 \le A \le 10000$

### Example input
    6
    4 9 2 5 13 10

### Example output
    5 -7 3 8 -3
    -12 10 5 -11

### Explanation of the example

