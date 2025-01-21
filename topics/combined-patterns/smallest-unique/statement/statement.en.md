## Smallest Unique
Some children play a game where everyone secretly writes a positive number on a piece of paper. The winner is the person who writes the smallest number that no one else writes. Given the list of numbers written down, decide the winning number! If there is no winner, print -1.

### Input
The first line of the input contains a single integer: $N$.
The second line of the input contains $N$ integers: $A_1, A_2, \ldots, A_N$, the numbers written by the children.

### Output
Print the smallest number that occurs only once in the sequence. If there is no such number then print -1.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 100$

### Example input
    7
    2 4 5 2 2 5 6

### Example output
    4

### Explanation of the example
The smallest number is 2, but it occurs more than once. 4 is the second smallest number and occurs only once, so 4 is the solution.
